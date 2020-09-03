from lark import Lark, tree, Transformer
import base64
import zlib

with open('grammar/grc.lark') as f:
    grammar = f.read()

parser = Lark(grammar, start='grc')

#grctest = "GRC1|BNINT,AOEM,FNGC,RU,TCON,CPLA,V000|PUSD,DSHCSMKTXTSmoking_home,MCHPLED|20200829MCHPHyperBoot,20200829MLEDCtrlr,20200829SSHLOEMTop,20200829SSHLOEMHsd,20211224RMSCMHyperBoot,20211224SMSCOEMCtrlport3,20211224SDDA3RD,|"
#grcztest = "eJxdzUGLwjAQhuE/NIdWD7tXk1QtJDVkEpW9DLIbbaE2pY2I0h9vBHdhvc4zvN/K8HxiVVlZWGwKBctKIBgHttxL4KpisOXkrCSHX5RP2qEAgWuUXIPCpYIC11KUK1Nou7fG90MgrH3bTrNslmWf+QemrELODhF+T0ZzpneG+jBEGvyxDdc/e/6W3RjJdfJw6b7rl8xzTBtpzIaeWIg1Nj9+fMcEMZwpBZL+w5QVzamJzd0P74Dx1l7G6QEucFGv"
#p = parser.parse(grcztest)
#grcdecoded = zlib.decompress(base64.b64decode(grcztest)).decode("utf-8")
#print(grcdecoded)
grcdecoded = "GRC1|BNINT,AOEM,FNDS,RU,TIXL,CMNB,VC_UTL_USZ_1|PUSD,DSHSLCP,MSFM,ESHLDIGREPTXTRepro_Shell|20200817SOEMMSCBat,20200817RPCBPWR_port_reflow,20200817MMSCInst_UnLaunch,20200831SREPSHLTop_BothSides,20200831SREPSHLBottom_Inside,20200831SREPMSCDigitizer,20200831SREPMSCStylus|"
p = parser.parse(grcdecoded)
class RepairTransformer(Transformer):
    pass


print(p.pretty())
