# """Demo"""

from datatoken.web3.wallet import Wallet
from datatoken.model.keeper import Keeper
from datatoken.model.constants import Role, Operation


keeper = Keeper()

system = Wallet(
    keeper.web3, private_key='0x1e771da3a1dcae0fd77a942cc816fd6b9b4cca97220f8ea6c6782a848714129d')
org1 = Wallet(
    keeper.web3, private_key='0x65e5b356ab8369c2971d584ade019c84d898f9b5d77d35940813c24a804d3b43')
user1 = Wallet(
    keeper.web3, private_key='0x243ba7d269e52c5861aca39cfa21cc94c75d43ad4189d666c06bae590a3a5317')
user2 = Wallet(
    keeper.web3, private_key='0xc679156774b1ea1ce27e00ea82efd3a1c5ad48d314abae0d1226452546679422')

#####
print('add role')
if not keeper.role_controller.check_role(
        org1.address, Role.ROLE_ENTERPRISE):
    keeper.role_controller.add_role(
        org1.address, Role.ROLE_ENTERPRISE, system)

print(keeper.role_controller.check_role(
    org1.address, Role.ROLE_ENTERPRISE))

print(keeper.role_controller.check_permission(
    org1.address, Operation.MODIFY_ASSET))

if not keeper.role_controller.check_role(
        user1.address, Role.ROLE_PROVIDER):
    keeper.role_controller.add_role(
        user1.address, Role.ROLE_PROVIDER, system)

print(keeper.role_controller.check_role(
    user1.address, Role.ROLE_PROVIDER))
print(keeper.role_controller.check_permission(
    user1.address, Operation.MODIFY_AUTHORIZE))

#####
print('register enterprise')
if not keeper.asset_provider.check_enterprise(org1.address):
    keeper.asset_provider.register_enterprise(
        org1.address, 'org1', 'test_org1', system)

print(keeper.asset_provider.check_enterprise(org1.address))
print(keeper.asset_provider.get_enterprise(org1.address))

keeper.asset_provider.update_enterprise(
    org1.address, 'org1', 'test_org1_update', system)
print(keeper.asset_provider.get_enterprise(org1.address))

#####
print('add provider')
if not keeper.asset_provider.check_provider(user1.address):
    keeper.asset_provider.add_provider(user1.address, system)
if not keeper.asset_provider.check_provider(user2.address):
    keeper.asset_provider.add_provider(user2.address, system)
if not keeper.asset_provider.check_provider(org1.address):
    keeper.asset_provider.add_provider(org1.address, system)

print(keeper.asset_provider.check_provider(user1.address))

#####
print('publish template')
tid = '0x7465737400000000000000000000000000000000000000000000000000000000'
checksum_test = '0x7465737400000000000000000000000000000000000000000000000000000000'

if not keeper.op_template.is_template_exist(tid):
    keeper.op_template.publish_template(
        tid, 'op1', checksum_test, 'ipfs_path_url1', system)

print(keeper.op_template.is_template_exist(tid))
print(keeper.op_template.get_template(tid))

print('update template')
keeper.op_template.update_template(
    tid, 'op2', checksum_test, 'ipfs_path_url2', system)
print(keeper.op_template.get_template(tid))

# #####
print('mint dts')
dt1 = '0x7465737400000000000000000000000000000000000000000000000000000011'
dt2 = '0x7465737400000000000000000000000000000000000000000000000000000022'
dt3 = '0x7465737400000000000000000000000000000000000000000000000000000033'
dt4 = '0x7465737400000000000000000000000000000000000000000000000000000044'
checksum_test = '0x7465737400000000000000000000000000000000000000000000000000000000'

keeper.dt_factory.mint_dt(dt1, user1.address,
                          True, checksum_test, 'ipfs_path_url1', org1)
print(keeper.dt_factory.check_dt_available(dt1))
print(keeper.dt_factory.get_dt_register(dt1))

keeper.dt_factory.mint_dt(dt2, user2.address,
                          True, checksum_test, 'ipfs_path_url2', org1)
print(keeper.dt_factory.check_dt_available(dt2))
print(keeper.dt_factory.get_dt_register(dt2))

keeper.dt_factory.mint_dt(dt3, org1.address,
                          False, checksum_test, 'ipfs_path_url3', org1)
print(keeper.dt_factory.check_dt_available(dt3))
print(keeper.dt_factory.get_dt_register(dt3))

keeper.dt_factory.mint_dt(dt4, org1.address,
                          False, checksum_test, 'ipfs_path_url4', org1)

print(keeper.dt_factory.get_owner_assets(org1.address))

#####
print('grant asset')
keeper.dt_factory.grant_dt(dt1, dt3, user1)
keeper.dt_factory.grant_dt(dt2, dt3, user2)
keeper.dt_factory.grant_dt(dt1, dt4, user1)
print(keeper.dt_factory.check_dt_perm(dt1, dt2))
print(keeper.dt_factory.check_dt_perm(dt1, dt3))
print(keeper.dt_factory.check_dt_perm(dt2, dt3))
print(keeper.dt_factory.check_dt_perm(dt1, dt4))

print(keeper.dt_factory.get_dt_grantees(keeper.web3.toBytes(hexstr=dt1)))

print('mint composable dt, succeed')
print(keeper.dt_factory.check_cdt_available(dt3))
keeper.dt_factory.start_compose_dt(dt3, [dt1, dt2], org1)
print(keeper.dt_factory.check_cdt_available(dt3))

#####
print('create task and job')
task_id = keeper.task_market.create_task('test', 'test_task', org1)
print(task_id)
print(keeper.task_market.get_task(task_id))
job_id = keeper.task_market.add_job(dt3, task_id, org1)
print(job_id)
print(keeper.task_market.get_job(job_id))

job_id = keeper.task_market.add_job(dt3, task_id, org1)
print(job_id)
print(keeper.task_market.get_job(job_id))

print(keeper.task_market.get_cdt_jobs(keeper.web3.toBytes(hexstr=dt3)))

#####
print('marketplace info')
print(keeper.dt_factory.get_dt_num())
print(keeper.op_template.get_template_num())
print(keeper.task_market.get_job_num())
print(keeper.task_market.get_task_num())

dt_idx, owners, issuers, checksums, isLeafs, ipfsPaths, _ = keeper.dt_factory.get_available_dts()
print(dt_idx)

print(keeper.asset_provider.get_issuer_names(issuers))

#####
print()
print('successfully finished')
