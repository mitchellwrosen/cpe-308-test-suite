import os
import shutil
import sys

# Ensures this script is run in a directory with a markup/ and a src/.
def SanityCheck():
  _, dirnames, _ = os.walk('.').next()
  if 'markup' not in dirnames or 'src' not in dirnames:
    print '%s must be run inside a directory with a markup/ and a src/.' % (
        os.path.basename(__file__))
    sys.exit(1)

# Generates .html files from .md files in markup/.
def GenerateHtml():
  # TODO(mitchell): This function.
  pass

# Moves .html files generated by markup from markup/ to their corresponding
# location in src/.
def MoveHtml():
  for dirpath, _, filenames in os.walk('markup'):
    for filename in filenames:
      if filename.endswith('.html'):
        src = os.path.join(dirpath, filename)
        # Better than src.replace('markup/', 'src/') because there may be more
        # than one 'markup/' in src.
        dst = 'src/' + src[7:]

        print '%s -> %s' % (src, dst)
        try:
          shutil.move(src, dst)
        except Exception, e:
          print '  %s. Did you forget to mkdir %s/?' % (e, dst[:dst.rfind('/')])

def main():
  SanityCheck()
  GenerateHtml()
  MoveHtml()

if __name__ == '__main__':
  main()
