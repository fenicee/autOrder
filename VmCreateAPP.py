import base64
import json
import re
import sys
import time
from enum import Enum

import PySide6
import pandas as pd
import rsa
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from ecloudsdkims.v1.list_image_resp_sample import ListImageRespSample
from ecloudsdkims.v1.list_share_image_sample import ListShareImageSample

from AppUi import Ui_MainWindow
from ecloudsdkecs.v1.model import *
from ecloudsdkims.v1.model import *
from VmCreateapiSample import VmCreateapiSample
from createSignature import RequestMsgByUrl
from vpcQuery import Vpc

Suzhou = "CIDC-RP-25"
Guangzhou3 = "CIDC-RP-26"
Chengdu =  "CIDC-RP-27"
Zhengzhou  = "CIDC-RP-28"
Beijing3 = "CIDC-RP-29"
Changsha2 = "CIDC-RP-30"
Jinan = "CIDC-RP-31"
Xian  = "CIDC-RP-32"
Shanghai1 = "CIDC-RP-33"
Chongqing = "CIDC-RP-34"
Hangzhou = "CIDC-RP-35"
Huhehaote = "CIDC-RP-48"
Guiyang = "CIDC-RP-49"

CNorth = [Huhehaote,Beijing3]
CNmid = [Zhengzhou,Changsha2]
CNeast = [Suzhou,Jinan,Shanghai1,Hangzhou]
CNwestsouth = [Guiyang,Chengdu,Chongqing]
CNsouth = [Guangzhou3]
CNorthwest = [Xian]
cityes = [Suzhou,Guangzhou3,Chengdu,Zhengzhou,Beijing3,Changsha2,Jinan,Xian,Shanghai1,Chongqing,Hangzhou,Huhehaote,Guiyang]
vmTypeList = {
"通用型" :"common" ,"通用入门型" : "commonIntroductory"
}
AviableRegion = {"CIDC-RP-25":['WXJD','SZJD'],"CIDC-RP-26":['DGJD'],"CIDC-RP-27":['CDJD'],"CIDC-RP-28":['ZZHKG','ZZGXQ'],"CIDC-RP-29":['BJJD']
                 ,"CIDC-RP-30":['CSZZ'],"CIDC-RP-31":['N0531-SD-JNSC01'],"CIDC-RP-32":['N029-SX-XAXX01'],"CIDC-RP-33":['N021-SH-MHZQ01'],
                 "CIDC-RP-34":['N023-CQ-BBST01'],"CIDC-RP-35":['N0574-ZJ-NBZD01'],"CIDC-RP-48":['N0471-NMG-HHHT01'],"CIDC-RP-490":['N0851-GZ-GYGZ01']}


class createVM_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() +"使用步骤如下:")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "一、Accesskey和SecretKey获取")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "登入移动云官网，控制台搜索‘云API’进入控制台界面，"
                                                                             "点击创建，注意创建完后会提示下载一个表格。")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "打开表格获取即可")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "二、查询所选节点是否有该配置")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "勾选要查询的节点，输入订购时长，数量，规格名称。选择系统盘类型"
                                                                             "并输入系统盘大小后即可查询")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "规格名称查询方法：在打开移动云在云主机订购界面的规格那栏就可以找到"
                                                                             "，例:t2.medium.2")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "以上填写完毕后需要进行询价前检查，‘询价前检查’按钮只有当验证Accesskey和"
                                         "secretkey后才可以解锁可用")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "点击‘询价前检查’，当通过后可解锁询价按钮")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "三、订购")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "和询价的功能步骤类似，填写资料=》订购前检查=》订购")
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        self.ui.akskvalidatebtn.clicked.connect(self.checkAkandSk)
        self.ui.locKeybtn.clicked.connect(self.locKey)
        self.ui.textEditArea.setReadOnly(True)
        self.ui.orderbtn.clicked.connect(self.orderVM)
        self.ui.isIpEnableCheckBox.clicked.connect(self.enableIp)
        self.ui.ecspasswordLineEdit.editingFinished.connect(self.checkPassword)
        self.ui.ecsNameLineEdit.editingFinished.connect(self.checkVmName)
        self.ui.queryPriceCheckbtn.clicked.connect(self.queryPriceCheck)
        self.ui.orderCheckbtn.clicked.connect(self.orderCheck)
        self.ui.queryExistVmbtn.clicked.connect(self.queryExitVm)
        self.ui.queryPriceBtn.clicked.connect(self.queryPrice)
        #询价按钮
        self.ui.queryPriceBtn.setEnabled(False)
        self.ui.orderbtn.setEnabled(False)
        self.ui.queryPriceCheckbtn.setEnabled(False)
        self.ui.orderCheckbtn.setEnabled(False)
        self.ui.queryExistVmbtn.setEnabled(False)
        self.rgnCheckboxdict = {self.ui.huhehaoteRegionCheckBox:Huhehaote,self.ui.beijingRegionCheckBox:Beijing3,self.ui.zhengzhouRegionCheckBox:Zhengzhou,
                           self.ui.changshaRegionCheckBox:Changsha2,self.ui.suzhouRegionCheckBox:Suzhou,self.ui.jinanRegionCheckBox:Jinan,
                           self.ui.shanghaiRegionCheckBox:Shanghai1,self.ui.hangzhouRegionCheckBox:Hangzhou,self.ui.guiyangRegionCheckBox:Guiyang,
                           self.ui.chengduRegionCheckBox:Chengdu,self.ui.chongqingRegionCheckBox:Chongqing,self.ui.guangzhouRegionCheckBox:Guangzhou3,
                           self.ui.xianRegionCheckBox:Xian}
        self.checkboxlist = [self.ui.huhehaoteRegionCheckBox,self.ui.beijingRegionCheckBox,self.ui.zhengzhouRegionCheckBox,self.ui.changshaRegionCheckBox,
                        self.ui.suzhouRegionCheckBox,self.ui.jinanRegionCheckBox,self.ui.shanghaiRegionCheckBox,self.ui.hangzhouRegionCheckBox,
                        self.ui.guiyangRegionCheckBox,self.ui.chengduRegionCheckBox,self.ui.chongqingRegionCheckBox,self.ui.guangzhouRegionCheckBox,
                        self.ui.xianRegionCheckBox]
        self.realnamedict = {
            self.ui.huhehaoteRegionCheckBox:"华北-呼和浩特",self.ui.beijingRegionCheckBox:"华北-北京",self.ui.zhengzhouRegionCheckBox:"华中-郑州",
            self.ui.changshaRegionCheckBox:"华中-长沙",self.ui.suzhouRegionCheckBox:"华东-苏州",self.ui.jinanRegionCheckBox:"华东-济南",self.ui.shanghaiRegionCheckBox:"华东-上海",self.ui.hangzhouRegionCheckBox:"华东-杭州",
                        self.ui.guiyangRegionCheckBox:"西南-贵阳",self.ui.chengduRegionCheckBox:"西南-成都",self.ui.chongqingRegionCheckBox:"西南-重庆",self.ui.guangzhouRegionCheckBox:"华南-广州",
                        self.ui.xianRegionCheckBox:"西北-西安"}
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + time.asctime(time.localtime(time.time())) + "----------初始化组件成功，欢迎使用")


    @Slot()
    def queryExitVm(self):
        ak = self.ui.acccesskeyLineEdit.text().strip()
        sk = self.ui.secretkeyLineEdit.text().strip()
        checkedbox = []
        for i in self.checkboxlist:
            if i.isChecked():
                checkedbox.append(i)
        if len(checkedbox) == 0:
            QMessageBox.warning(self, "警告", "请选择节点")
        else:
            regionList = []
            userNameList = []
            ecsNameList = []
            ipList = []
            createTimeList = []
            ecStatusList = []
            imageNameList = []
            vCpuList = []
            vMemoryList = []
            excelName = ""
            for eachEndpoint in checkedbox:
                client = VmCreateapiSample.create_client(ak, sk, self.rgnCheckboxdict[eachEndpoint])
                request = VmlistServerPortsDetailRespRequest
                vmresp_query = VmlistServerPortsDetailRespQuery
                server_types = ["VM","IRONIC","EBM"]
                product_types = ["NORMAL","DE_CLOUD","AUTOSCALING","VO","CDN","PAAS_MASTER","PAAS_SLAVE","EMR","VCPE","LOGAUDIT","MSE"]
                vmresp_query.visible = True
                vmresp_query.server_types = server_types
                vmresp_query.product_types = product_types
                request.vmlist_server_ports_detail_resp_query = vmresp_query
                res = client.vmlist_server_ports_detail_resp(request)
                if res.error_message != "" and res.body != None:
                    if res.body.total != 0:
                        for eachinfo in res.body.content:
                            regionList.append(self.realnamedict[eachEndpoint])
                            userNameList.append(eachinfo.user_name)
                            ecsNameList.append(eachinfo.name)
                            fipAddressList = []
                            for eachport_detail in eachinfo.port_detail:
                                if eachport_detail.fip_address != None :
                                    fipAddressList.append(eachport_detail.fip_address)
                            ipList.append(fipAddressList)
                            createTimeList.append(eachinfo.created_time)
                            ecStatusList.append(eachinfo.ec_status)
                            imageNameList.append(eachinfo.image_name)
                            vCpuList.append(eachinfo.vcpu)
                            vMemoryList.append(eachinfo.vmemory)
                        excelName = excelName + self.realnamedict[eachEndpoint] + ","
            if excelName != "":
                dfDataDict = {'地区': regionList, '用户名': userNameList, '云主机名': ecsNameList, '公网Ip地址': ipList,
                              '云主机创建时间': createTimeList, '云主机状态': ecStatusList, '镜像名': imageNameList,
                              'cpu数量': vCpuList, '内存大小（MB）': vMemoryList}
                dfData = pd.DataFrame(dfDataDict, index=None)
                dfData.to_excel('%s以上节点的订购情况.xlsx'%(excelName),index=False)
                QMessageBox.information(self, "消息","导出成功")

            else:
                QMessageBox.warning(self,"提醒","所选节点并无云主机信息")
                self.ui.textEditQueryVM.setMarkdown(self.ui.textEditArea.toMarkdown() + time.asctime(
                    time.localtime(time.time())) + "%s以上节点云主机信息已导出，请查看当前目录文件下的excel表格"%(excelName))
    @Slot()
    def checkPassword(self):
        passwdLength = len(self.ui.ecspasswordLineEdit.text())
        if passwdLength < 8 or passwdLength > 16 :
            QMessageBox.warning(self,"警告","密码应该是8-16位字符")
            self.ui.ecspasswordLineEdit.setText("")
            return False
        else :
            upper = re.findall('[A-Z]', self.ui.ecspasswordLineEdit.text())
            lower = re.findall('[a-z]', self.ui.ecspasswordLineEdit.text())
            number = re.findall('[0-9]', self.ui.ecspasswordLineEdit.text())
            special = re.findall('[\~\@\#\$\%\*\_\-\+\=\:\,\.\?\[\]\{\}]', self.ui.ecspasswordLineEdit.text())
            if len(upper) >0 and len(lower)>0 and len(number)>0 and len(special) >0 and len(special)<=3:
                QMessageBox.information(self, "信息",
                                    "密码合规")
                return True
            else:
                QMessageBox.warning(self, "警告", "密码同时包括数字、大小写字母和特殊字符，其中特殊字符最多不能超过3个，且需要在“~ @ # $ % * _ - + = : , . ? [ ] { }”范围内")
                self.ui.ecspasswordLineEdit.setText("")
                return False

    @Slot()
    def checkVmName(self):
        nameLength = len(self.ui.ecsNameLineEdit.text())
        if nameLength < 5 or nameLength > 22:
            QMessageBox.warning(self, "警告", "云主机名称为5-22位")
            self.ui.ecsNameLineEdit.setText("")
            return False
        else:
            upper = re.findall('[A-Z]', self.ui.ecsNameLineEdit.text().strip())
            lower = re.findall('[a-z]', self.ui.ecsNameLineEdit.text().strip())
            number = re.findall('[0-9]', self.ui.ecsNameLineEdit.text().strip())
            joinSymbol = re.match('^[^-].*-.*[^-]$',self.ui.ecsNameLineEdit.text().strip())
            if len(upper)+len(lower) > 0 and len(number) >0 and joinSymbol != None:
                QMessageBox.information(self, "信息",
                                        "名称合规")
                return True
            else:
                QMessageBox.warning(self, "警告", "云主机名称数字、字母、“-”组合，且“-”不可在名称的开头或结尾")
                self.ui.ecsNameLineEdit.setText("")
                return False
    @Slot()
    def enableIp(self):
        if self.ui.isIpEnableCheckBox.checkState() == PySide6.QtCore.Qt.CheckState.Checked:
            self.ui.bandwidthChargeModeComboBox.setEnabled(True)
            self.ui.bandwidthSizeSpinBox.setEnabled(True)
            return
        else:
            self.ui.bandwidthChargeModeComboBox.setEnabled(False)
            self.ui.bandwidthSizeSpinBox.setEnabled(False)
            return


    @Slot()
    def queryPriceCheck(self):
        bootVolumeSize = self.ui.bootVolumeSizeLineEdit.text().strip()
        errmsg = []
        try:
            bootVolumeSize = int(bootVolumeSize)
        except:
            errmsg.append("----------（询价检查错误）系统盘参数非法请输入整数")
        if int(self.ui.durationSpinBox.value()) == 0 or int(self.ui.quantitySpinBox.value()) == 0:
            errmsg.append("----------（询价检查错误）订购时长/数量不能为0！")
        if self.ui.specsNameLineEdit.text().strip() == "":
            errmsg.append("----------（询价检查错误）规格名称不能为空！")
        if len(errmsg) >0:
            self.showMsgIntextArea("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            for eacherrmsg in errmsg:
                self.showMsgIntextArea(eacherrmsg)
            self.showMsgIntextArea("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            QMessageBox.warning(self, "警告", "检查失败，详情见左侧消息区域错误信息")
            return False
        else:
            QMessageBox.information(self, "提示", "检查成功，可以询价")
            self.ui.queryPriceBtn.setEnabled(True)
            return True

    @Slot()
    def orderCheck(self):
        checkedbox = []
        errmsg = []
        bootVolumeSize = self.ui.bootVolumeSizeLineEdit.text().strip()
        for i in self.checkboxlist:
            if i.isChecked():
                checkedbox.append(i)
        if len(checkedbox) == 0:
            errmsg.append("----------（订购检查错误）未选择订购的节点")
        if int(self.ui.durationSpinBox.value()) == 0 or int(self.ui.quantitySpinBox.value()) == 0:
            errmsg.append("----------（订购检查错误）订购时长/数量不能为0！")
        if self.ui.specsNameLineEdit.text().strip() == "":
            errmsg.append("----------（订购检查错误）规格名称不能为空")
        if int(self.ui.cpuSpinBox.value()) == 0 or int(self.ui.ramSpinBox.value()) == 0:
            errmsg.append("----------（订购检查错误）cpu/ram数量不能为0！")
        try:
            bootVolumeSize = int(bootVolumeSize)
        except:
            errmsg.append("----------（订购检查错误）系统盘参数非法请输入整数")
        if self.ui.ecspasswordLineEdit.text().strip() == "" or self.ui.ecsNameLineEdit.text().strip() == "":
            errmsg.append("----------（订购检查错误）云主机名/密码不能为空")
        if len(errmsg) > 0:
            self.showMsgIntextArea("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            for eacherrmsg in errmsg:
                self.showMsgIntextArea(eacherrmsg)
            self.showMsgIntextArea("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            QMessageBox.warning(self, "警告", "检查失败，详情见左侧消息区域错误信息")
            return False
        else:
            QMessageBox.information(self, "提示", "检查成功，可以订购")
            self.ui.orderbtn.setEnabled(True)
            return True

    @Slot()
    def orderVM(self):
        ak = self.ui.acccesskeyLineEdit.text().strip()
        sk = self.ui.secretkeyLineEdit.text().strip()
        checkedbox = []
        for i in self.checkboxlist:
            if i.isChecked():
                checkedbox.append(i)
        if len(checkedbox) == 0:
            QMessageBox.information(self, "提示", "请优先勾选节点")
        else:
            if self.ui.billingTypeComboBox.currentText() == "按月支付（包月）":
                billingType = "MONTH"
            elif self.ui.billingTypeComboBox.currentText() == "按年支付（包年）":
                billingType = "YEAR"
            else:
                billingType = "HOUR"

            vmType = vmTypeList[self.ui.vmTypeComboBox.currentText()]

            cpu = int(self.ui.cpuSpinBox.value())

            ram = int(self.ui.ramSpinBox.value())

            disk = int(self.ui.bootVolumeSizeLineEdit.text())

            specs = self.ui.specsNameLineEdit.text().strip()

            boot_volume = VmCreateapiRequestBootVolume()
            if self.ui.bootVolumeTypeComboBox.currentText() == "高性能型硬盘":
                volumeType = "highPerformance"
            else:
                volumeType = "performanceOptimization"

            boot_volume_size = int(self.ui.bootVolumeSizeLineEdit.text())

            duration = int(self.ui.durationSpinBox.value())

            quantity = int(self.ui.quantitySpinBox.value())

            with open('publickey.pem', mode='rb') as publicfile:
                keydata = publicfile.read()
            publickey = rsa.PublicKey.load_pkcs1_openssl_pem(keydata)
            password = self.ui.ecspasswordLineEdit.text().strip()
            vmName = self.ui.ecsNameLineEdit.text().strip()
            image_name = self.ui.imageNameComboBox.currentText()
            password = password.encode('utf8')
            crypto = rsa.encrypt(password, publickey)
            crypto = base64.encodebytes(crypto).decode('utf-8')


            for eachEndpoint in checkedbox:
                client = VmCreateapiSample.create_client(ak, sk, self.rgnCheckboxdict[eachEndpoint])
                request = VmCreateapiRequest()
                vmcreate_body = VmCreateapiBody()
                vmcreate_body.region = AviableRegion[self.rgnCheckboxdict[eachEndpoint]][0]
                vmcreate_body.billing_type = billingType
                vmcreate_body._vm_type = vmType
                vmcreate_body.cpu = cpu
                vmcreate_body.ram = ram
                vmcreate_body.disk = disk
                vmcreate_body.specs_name = specs

                boot_volume.size = boot_volume_size
                boot_volume.volume_type = volumeType

                vmcreate_body.boot_volume = boot_volume
                networks = VmCreateapiRequestNetworks()
                vpc = Vpc()
                networks.network_id = vpc.getNetworkId(ak, sk, self.rgnCheckboxdict[eachEndpoint])
                #判断是否订购了Ip
                #订购了Ip
                if self.ui.isIpEnableCheckBox.checkState() == PySide6.QtCore.Qt.CheckState.Checked:
                    # 弹性IP
                    ip = VmCreateapiRequestIp()
                    ip.ip_type = "MOBILE"
                    vmcreate_body.ip = ip
                    bandwith = VmCreateapiRequestBandwidth()
                    # 按带宽计费。
                    bandwithChargeMode = self.ui.bandwidthChargeModeComboBox.currentText()
                    if bandwithChargeMode == "按带宽计费":
                        bandwith.charge_mode = "bandwidthCharge"
                    else :
                        bandwith.charge_mode = "trafficCharge"
                    bandwith.bandwidth_size = int(self.ui.bandwidthSizeSpinBox.value())
                    vmcreate_body.bandwidth = bandwith
                else:
                    pass

                vmcreate_body.duration = duration
                vmcreate_body.quantity = quantity
                vmcreate_body._networks = networks
                vmcreate_body.password = crypto
                vmcreate_body.image_name = image_name
                vmcreate_body.name = vmName
                request.vm_create_body = vmcreate_body
                try:
                    data = client.vm_createapi(request)
                    if data.body == None:
                        print(data)
                        self.showMsgIntextArea("----------%s节点订购失败。原因:%s" % (
                                                                self.realnamedict[eachEndpoint], data.error_message))
                except Exception as e:
                    print("订购成功,生成了订单")
                    self.showMsgIntextArea("----------%s节点订购成功。"% (self.realnamedict[eachEndpoint]))
                    self.ui.orderbtn.setEnabled(False)


    def showMsgIntextArea(self,msg):
        self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown()+time.asctime(
                        time.localtime(time.time()))+msg)

    @Slot()
    def queryPrice(self):
        checkedbox = []
        for i in self.checkboxlist:
            if i.isChecked():
                checkedbox.append(i)
        if len(checkedbox) == 0 :
            QMessageBox.information(self,"提示","请优先勾选节点")
        else:
            self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            # queryPriceClient = VmqueryPriceSample
            # request = VmqueryPriceRequest
            if self.ui.bootVolumeTypeComboBox.currentText() == "高性能型硬盘":
                volumeType = "highPerformance"
            else:
                volumeType = "performanceOptimization"
            if self.ui.billingTypeComboBox.currentText() == "按月支付（包月）":
                billingType = "month"
            elif self.ui.billingTypeComboBox.currentText() == "按年支付（包年）":
                billingType = "year"
            else:
                billingType = "hour"
            data = {
                "productType":"vm",
                "bootVolume":{
                    "size":int(self.ui.bootVolumeSizeLineEdit.text()),
                    "volumeType":volumeType
                },
                "specsName":self.ui.specsNameLineEdit.text().strip(),
                "quantity":int(self.ui.quantitySpinBox.value()),
                "duration":int(self.ui.durationSpinBox.value()),
                "feeUnit":billingType
            }
            for checkedcity in checkedbox:
                requesturl = RequestMsgByUrl(self.ui.acccesskeyLineEdit.text().strip(), self.ui.secretkeyLineEdit.text().strip(),'POST',
                                             self.rgnCheckboxdict[checkedcity], "/api/v2/server/query/price", data)
                res = requesturl.requestByUrl()
                if res['body']!= None :
                    price = float(res['body']['serverPrice'].replace(',',''))+float(res['body']['bootVolumePrice'].replace(',',''))
                    self.showMsgIntextArea("----------%s节点该配置价格为 %.2f元(只包含云主机和硬盘价格)" % (
                                                     self.realnamedict[checkedcity], price))

                else:
                    self.showMsgIntextArea("----------%s节点询价失败。原因:%s" % (
                                                     self.realnamedict[checkedcity], res['errorMessage']))
            self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            self.ui.queryPriceBtn.setEnabled(False)

    @Slot()
    def locKey(self):
        isakReadOnly =self.ui.acccesskeyLineEdit.isReadOnly()
        iskReadOnly = self.ui.secretkeyLineEdit.isReadOnly()
        if isakReadOnly == False and iskReadOnly == False :
            self.ui.acccesskeyLineEdit.setReadOnly(True)
            self.ui.secretkeyLineEdit.setReadOnly(True)
            self.ui.acccesskeyLineEdit.setStyleSheet("background-color: rgb(171, 171, 171)")
            self.ui.secretkeyLineEdit.setStyleSheet("background-color: rgb(171, 171, 171)")
            QMessageBox.information(self, "提示", "锁定成功")
        else :
            self.ui.acccesskeyLineEdit.setReadOnly(False)
            self.ui.secretkeyLineEdit.setReadOnly(False)
            QMessageBox.information(self,"提示","解锁成功")
            self.ui.acccesskeyLineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.ui.secretkeyLineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")

    @Slot()
    def checkAkandSk(self):
        ak = self.ui.acccesskeyLineEdit.text().strip()
        sk = self.ui.secretkeyLineEdit.text().strip()
        if ak != "" and sk != "" :
            client = VmCreateapiSample.create_client(ak,sk,
                                             "CIDC-RP-35")
            request = VmCreateapiRequest()
            res = client.vm_createapi(request)
            if ("Invalid parameter AccessKey " == res.error_message or "Invalid parameter Signature " == res.error_message):
                QMessageBox.critical(self, "错误", "accesskey或者secretkey错误，请重新输入")
                self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown()+time.asctime( time.localtime(time.time()) )+"----------accesskey或者secretkey错误，请重新输入")
            else:
                QMessageBox.information(self, "成功", "验证正确")
                self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + time.asctime(
                    time.localtime(time.time())) + "----------accesskey,secretkey验证正确")
                self.ui.acccesskeyLineEdit.setReadOnly(True)
                self.ui.secretkeyLineEdit.setReadOnly(True)
                self.ui.acccesskeyLineEdit.setStyleSheet("background-color: rgb(171, 171, 171)")
                self.ui.secretkeyLineEdit.setStyleSheet("background-color: rgb(171, 171, 171)")
                self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + time.asctime(
                    time.localtime(time.time())) + "----------accesskey,secretkey已锁定")
                self.ui.queryPriceCheckbtn.setEnabled(True)
                self.ui.orderCheckbtn.setEnabled(True)
                self.ui.queryExistVmbtn.setEnabled(True)
                #刷新镜像列表
                self.getAllImage()
        else:
            QMessageBox.critical(self,"错误","accesskey或者secretkey为空，请重新输入")
            self.ui.textEditArea.setMarkdown(self.ui.textEditArea.toMarkdown() + time.asctime(
                time.localtime(time.time())) + "----------accesskey或者secretkey为空，请重新输入")

    #获取所有镜像
    def getAllImage(self):
        addImage = []
        ak = self.ui.acccesskeyLineEdit.text().strip()
        sk = self.ui.secretkeyLineEdit.text().strip()
        for eachEndpoint in self.checkboxlist:
            selfclient = ListImageRespSample.create_client(ak,sk,self.rgnCheckboxdict[eachEndpoint])
            shareclient = ListShareImageSample.create_client(ak,sk,self.rgnCheckboxdict[eachEndpoint])
            selfrequest = ListImageRespRequest
            sharerequest = ListShareImageRequest
            shareres = shareclient.list_share_image(sharerequest)
            selfres = selfclient.list_image_resp(selfrequest)
            if shareres != None and shareres.body != None and len(shareres.body.content) != 0 :
                for eachImage in shareres.body.content:
                    addImage.append(eachImage.name)
                    self.showMsgIntextArea("========== %s节点存在共享镜像 %s"%(
                    self.realnamedict[eachEndpoint], eachImage.name))
            if selfres != None and selfres.body != None and len(selfres.body.content) != 0 :
                for eachImages in selfres.body.content:
                    addImage.append(eachImages.name)
                    self.showMsgIntextArea("---------- %s节点存在私有镜像 %s"%(self.realnamedict[eachEndpoint],eachImages.name))
        self.ui.imageNameComboBox.clear()
        self.ui.imageNameComboBox.addItem("CentOS 7.9 64位")
        self.ui.imageNameComboBox.addItem("Ubuntu 20.04 64位")
        self.ui.imageNameComboBox.addItem("Red Hat Enterprise Linux8.1 64位")
        self.ui.imageNameComboBox.addItem("Windows Server 2019 DataCenter 64位 中文版")
        self.ui.imageNameComboBox.addItem("BC-Linux 8.1 64位")
        self.ui.imageNameComboBox.addItem("BC-Linux 8.2 64位")
        self.ui.imageNameComboBox.addItem("CoreOS 2303.4.0 64位")
        self.ui.imageNameComboBox.addItem("Debian 9.11 64位")
        self.ui.imageNameComboBox.addItem("FreeBSD 12.1 64位")
        self.ui.imageNameComboBox.addItem("OpenSUSE 42.3 64位")
        self.ui.imageNameComboBox.addItem("SUSE Linux Enterprise Server 12 SP5 64位")
        for i in addImage:
            self.ui.imageNameComboBox.addItem(i)




def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = createVM_window()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()