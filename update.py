import os
import subprocess
import sys


# Ensures markdown is installed and this script is run in a directory with a
# markdown/.
def SanityCheck():
  if subprocess.call(['which', 'markdown'], stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE):
    print 'markdown not installed. Type: sudo apt-get install markdown'
    return False

  _, dirnames, _ = os.walk('.').next()
  if 'markdown' not in dirnames:
    print './markdown/ not found.'
    return False

  return True

# Updates .html files from .md files in markdown/.
def UpdateHtml():
  for dirpath, _, filenames in os.walk('./markdown'):
    for filename in filenames:
      if filename.endswith('.md'):
        src = os.path.join(dirpath, filename)
        dst = src.replace('./markdown/', './').replace('.md', '.html')

        p = subprocess.Popen(['markdown', src], stdout=subprocess.PIPE)

        html, err = p.communicate()
        if err:
          print 'markdown %s > %s' % (src, dst)
          print '  [ERROR]: %s' % err
          continue

        auto_gen_comment = ('<!--\n'
                            '   Automatically generated from %s.\n'
                            '   DO NOT EDIT!\n'
                            '-->\n' % src)
        html = auto_gen_comment + html

        f = open(dst, 'w')
        f.write(html)
        f.close()

def main():
  if not SanityCheck():
    return 1

  UpdateHtml()

if __name__ == '__main__':
  main()
