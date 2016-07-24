#!/usr/bin/env python2

import re
import sys
import json
import subprocess

executable = "${TESTPROG}"

def parse_test(raw):
	raw = re.compile('#.*$', re.M).sub('', raw).strip()
	if raw.startswith('"""'):
		raw = raw[3:]

	for fixture in raw.split('r"""'):
		name = ''
		doc, _, body = fixture.partition('"""')
		cases = []
		for case in body.split('$')[1:]:
			argv, _, expect = case.strip().partition('\n')
			expect = json.loads(expect)
			prog, _, argv = argv.strip().partition(' ')
			cases.append((prog, argv, expect))

		yield name, doc, cases

failures = 0
passes = 0

tests = open('${TESTCASES}','r').read()
for _, doc, cases in parse_test(tests):
	if not cases: continue

	for prog, argv, expect in cases:
		args = [ x for x in argv.split() if x ]

		expect_error = not isinstance(expect, dict)

		error = None
		out = None
		try:
			out = subprocess.check_output([executable, doc]+args, stderr=subprocess.STDOUT)
			if expect_error:
				error = " ** an error was expected but it appeared to succeed!"
			else:
				json_out = json.loads(out)
				if expect != json_out:
					error = " ** JSON does not match expected: %r" % expect
		except subprocess.CalledProcessError as e:
			if not expect_error:
				error = "\n ** this should have succeeded! exit code = %s" % e.returncode

		if not error:
			passes += 1
			continue

		failures += 1

		print "="*40
		print doc
		print ':'*20
		print prog, argv
		print '-'*20
		if out:
			print out
		print error

if failures:
	print "%d failures" % failures
	sys.exit(1)
else:
	print "PASS (%d)" % passes
