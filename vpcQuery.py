import time

from ecloudsdkvpc.v1 import ListNetworkRespRequest, CreateNetworkRequest, CreateNetworkBody, VpcOrderRequest, \
    VpcOrderRequestSubnets, VpcOrderBody, ListVpcRespRequest, ListVpcRespQuery, ListSubnetRespRequest, \
    CreateNetworkRequestSubnets
from ecloudsdkvpc.v1.create_network_sample import CreateNetworkSample
from ecloudsdkvpc.v1.list_subnet_resp_sample import ListSubnetRespSample
from ecloudsdkvpc.v1.list_vpc_resp_sample import ListVpcRespSample
from ecloudsdkvpc.v1.vpc_order_sample import VpcOrderSample


class Vpc:
    Suzhou = "CIDC-RP-25"
    Guangzhou3 = "CIDC-RP-26"
    Chengdu = "CIDC-RP-27"
    Zhengzhou = "CIDC-RP-28"
    Beijing3 = "CIDC-RP-29"
    Changsha2 = "CIDC-RP-30"
    Jinan = "CIDC-RP-31"
    Xian = "CIDC-RP-32"
    Shanghai1 = "CIDC-RP-33"
    Chongqing = "CIDC-RP-34"
    Hangzhou = "CIDC-RP-35"
    Huhehaote = "CIDC-RP-48"
    Guiyang = "CIDC-RP-49"

    AviableRegion = {"CIDC-RP-25": ['WXJD', 'SZJD'], "CIDC-RP-26": ['DGJD'], "CIDC-RP-27": ['CDJD'],
                     "CIDC-RP-28": ['ZZHKG', 'ZZGXQ'], "CIDC-RP-29": ['BJJD']
        , "CIDC-RP-30": ['CSZZ'], "CIDC-RP-31": ['N0531-SD-JNSC01'], "CIDC-RP-32": ['N029-SX-XAXX01'],
                     "CIDC-RP-33": ['N021-SH-MHZQ01'],
                     "CIDC-RP-34": ['N023-CQ-BBST01'], "CIDC-RP-35": ['N0574-ZJ-NBZD01'],
                     "CIDC-RP-48": ['N0471-NMG-HHHT01'], "CIDC-RP-490": ['N0851-GZ-GYGZ01']}

    def queryVpc(ak,sk,poolid):
        vpcqueryclient = ListVpcRespSample.create_client(ak,
                                                         sk, poolid)
        queryrequest = ListVpcRespRequest()
        list_vpc_resp_query = ListVpcRespQuery()
        tag_ids = [""]
        list_vpc_resp_query.tag_ids = tag_ids
        queryrequest.list_vpc_resp_query = list_vpc_resp_query
        return vpcqueryclient.list_vpc_resp(queryrequest)

    def addvpc(ak,sk,poolid):
        vpcorderclient = VpcOrderSample.create_client(ak,sk,poolid)
        addvpcrequest = VpcOrderRequest()
        vpcbody = VpcOrderBody()
        vpcbody.name = "testvpc"
        vpcbody.network_name = "network01"
        vpcbody.specs = "high"
        vpcbody.region = Vpc.AviableRegion[poolid][0]
        addvpcrequest.vpc_order_body = vpcbody
        return vpcorderclient.vpc_order(addvpcrequest)

    def listSubnetResp(ak,sk,poolid):
        subnetQueryClient = ListSubnetRespSample.create_client(ak,sk,poolid)
        listSubnetQueryRequest = ListSubnetRespRequest()
        return subnetQueryClient.list_subnet_resp(listSubnetQueryRequest)

    def addSubnet(ak,sk,poolid,router_id):
        createSubnetClient = CreateNetworkSample.create_client(ak,sk,poolid)
        createNetworkRequest = CreateNetworkRequest()
        create_network_body = CreateNetworkBody()
        create_network_body.availability_zone_hints = Vpc.AviableRegion[poolid][0]
        create_network_body.network_name = "testsubnet"
        create_network_body.network_type_enum = "VM"
        create_network_body.region = Vpc.AviableRegion[poolid][0]
        create_network_body.router_id = router_id
        subnets = []
        subnets.append(CreateNetworkRequestSubnets(ip_version="4",cidr="192.168.1.0/24",subnet_name="testsubnet")
        )
        create_network_body.subnets = subnets
        createNetworkRequest.create_network_body = create_network_body
        return createSubnetClient.create_network(createNetworkRequest)

    def getNetworkId(self,ak,sk,poolid):
        # ak = "7bee2d8d0a38429dbaaade711bc42baf"
        # sk = "9a7bd2bb5f50488eb16dcb0547b12435"
        # poolid = Guangzhou3
        vpcquerytest = Vpc.queryVpc(ak,sk,poolid)
        #没有Vpc
        if  vpcquerytest.body.content == None:
            Vpc.addvpc(ak,sk,poolid)
            vpcquerytest = Vpc.queryVpc(ak,sk,poolid)
            Vpc.addSubnet(ak, sk, poolid, vpcquerytest.body.content[0].router_id)
        else:
            if  len(Vpc.listSubnetResp(ak,sk,poolid).body.content) == 0:
                #需要新增
               Vpc.addSubnet(ak,sk,poolid,vpcquerytest.body.content[0].router_id)
        return Vpc.listSubnetResp(ak,sk,poolid).body.content[0].network_id

# def main():
#     vpc = Vpc()
#     print(vpc.getNetworkId("7bee2d8d0a38429dbaaade711bc42baf","9a7bd2bb5f50488eb16dcb0547b12435","CIDC-RP-26"))
#
#
# if __name__ == "__main__":
#     main()