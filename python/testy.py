from keepass import kpdb

db = kpdb.Database('/Users/phinze/dev/setec_astronomy/spec/test_database.kdb', 'testmasterpassword')
print db.header.encryption_type()
for group in db.groups:
    print group.name()
for entry in db.entries:
    print entry.password
print 'DONE'
