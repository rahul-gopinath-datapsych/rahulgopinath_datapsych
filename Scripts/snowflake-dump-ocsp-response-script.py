#!c:\users\rahul\appdata\local\programs\python\python37-32\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'snowflake-connector-python==2.2.1','console_scripts','snowflake-dump-ocsp-response'
__requires__ = 'snowflake-connector-python==2.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('snowflake-connector-python==2.2.1', 'console_scripts', 'snowflake-dump-ocsp-response')()
    )
