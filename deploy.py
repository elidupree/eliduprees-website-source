#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import subprocess

prod_server = 'future.elidupree.com'

def upload_to_future():
  a = './build/idupree_websitepy_output/build/nginx/deploy/'
  b = 'elidupreecom-test-deploy@'+prod_server+':'
  rargs = ['rsync', '-azv', '--progress', a, b]
  subprocess.check_call(rargs + ['--delay-updates'])
  subprocess.check_call(['ssh', '-T', 'reload-nginx@'+prod_server])
  subprocess.check_call(rargs + ['--delete'])

def upload_to_prod():
  a = './build/idupree_websitepy_output/build/nginx/deploy/'
  b = 'elidupreecom-deploy@'+prod_server+':'
  rargs = ['rsync', '-azv', '--progress', a, b]
  subprocess.check_call(rargs + ['--delay-updates'])
  subprocess.check_call(['ssh', '-T', 'reload-nginx@'+prod_server])
  subprocess.check_call(rargs + ['--delete'])


def main():
  if '--future' in sys.argv:
    upload_to_future()
  if '--prod' in sys.argv:
    ready = False
    with open ("./build/initial/deploy_ready") as deploy_file:
      if deploy_file.read () == "yes":
        ready = True
    if not ready:
      print ("Not ready for deployment. Run `./build.py --deploy` first.")
    else:
      upload_to_prod()

if __name__ == '__main__':
  main()


