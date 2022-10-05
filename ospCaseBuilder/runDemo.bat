ospCaseBuilder caseDict --graph
cosim run OspSystemStructure.xml -b 0 -d 10 --real-time --log-level info
watchCosim watchDict -pd
