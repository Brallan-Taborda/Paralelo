import numpy as np
from numpy import *
import subprocess
import ray

#inicializacion de ray
ray.init(num_cpus=8)

#funcion para escribir un documento
def writeinputf(file,dictionary):
    ''' write dictionarys parameters in file'''
    data1 = open(file,'w')
    for items in dictionary.items():
        data1.write("%s %s\n" % items)

    data1.close()

#funciones a paralelizar (usan micrOMEGAS 5.2)
@ray.remote
def proceso1():
    newlist1=[ ]
    datapar1={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar1['la41']=LA41
    datapar1['la42']=LA42
    datapar1['la412']=LA412
    datapar1['la31']=LA31
    datapar1['la32']=LA32
    datapar1['laS1']=LAS1
    datapar1['laS2']=LAS2
    datapar1['muSS1']=MUSS1
    datapar1['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar1['Mdm1']=Mphi1
        datapar1['Mdm2']=Mphi2
        datapar1['laS1']=LAS1
        datapar1['laS2']=LAS2
        datapar1['muSS1']=MUSS1
        #
        writeinputf('data1.dat',datapar1)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main1 data1.dat > output1.dat")
        aa=subprocess.getoutput("grep Omega_1 output1.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output1.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output1.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output1.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output1.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output1.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output1.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output1.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output1.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output1.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output1.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist1.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos1 = np.asarray(newlist1)
    np.savetxt('proceso1.txt',datos1)

@ray.remote
def proceso2():
    newlist2=[ ]
    datapar2={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar2['la41']=LA41
    datapar2['la42']=LA42
    datapar2['la412']=LA412
    datapar2['la31']=LA31
    datapar2['la32']=LA32
    datapar2['laS1']=LAS1
    datapar2['laS2']=LAS2
    datapar2['muSS1']=MUSS1
    datapar2['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar2['Mdm1']=Mphi1
        datapar2['Mdm2']=Mphi2
        datapar2['laS1']=LAS1
        datapar2['laS2']=LAS2
        datapar2['muSS1']=MUSS1
        #
        writeinputf('data2.dat',datapar2)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main2 data2.dat > output2.dat")
        aa=subprocess.getoutput("grep Omega_1 output2.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output2.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output2.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output2.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output2.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output2.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output2.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output2.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output2.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output2.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output2.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist2.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos2 = np.asarray(newlist2)
    np.savetxt('proceso2.txt',datos2)

@ray.remote
def proceso3():
    newlist3=[ ]
    datapar3={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar3['la41']=LA41
    datapar3['la42']=LA42
    datapar3['la412']=LA412
    datapar3['la31']=LA31
    datapar3['la32']=LA32
    datapar3['laS1']=LAS1
    datapar3['laS2']=LAS2
    datapar3['muSS1']=MUSS1
    datapar3['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar3['Mdm1']=Mphi1
        datapar3['Mdm2']=Mphi2
        datapar3['laS1']=LAS1
        datapar3['laS2']=LAS2
        datapar3['muSS1']=MUSS1
        #
        writeinputf('data3.dat',datapar3)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main3 data3.dat > output3.dat")
        aa=subprocess.getoutput("grep Omega_1 output3.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output3.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output3.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output3.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output3.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output3.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output3.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output3.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output3.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output3.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output3.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist3.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos3 = np.asarray(newlist3)
    np.savetxt('proceso3.txt',datos3)

@ray.remote
def proceso4():
    newlist4=[ ]
    datapar4={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar4['la41']=LA41
    datapar4['la42']=LA42
    datapar4['la412']=LA412
    datapar4['la31']=LA31
    datapar4['la32']=LA32
    datapar4['laS1']=LAS1
    datapar4['laS2']=LAS2
    datapar4['muSS1']=MUSS1
    datapar4['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar4['Mdm1']=Mphi1
        datapar4['Mdm2']=Mphi2
        datapar4['laS1']=LAS1
        datapar4['laS2']=LAS2
        datapar4['muSS1']=MUSS1
        #
        writeinputf('data4.dat',datapar4)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main4 data4.dat > output4.dat")
        aa=subprocess.getoutput("grep Omega_1 output4.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output4.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output4.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output4.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output4.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output4.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output4.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output4.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output4.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output4.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output4.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist4.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos4 = np.asarray(newlist4)
    np.savetxt('proceso4.txt',datos4)

@ray.remote
def proceso5():
    newlist5=[ ]
    datapar5={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar5['la41']=LA41
    datapar5['la42']=LA42
    datapar5['la412']=LA412
    datapar5['la31']=LA31
    datapar5['la32']=LA32
    datapar5['laS1']=LAS1
    datapar5['laS2']=LAS2
    datapar5['muSS1']=MUSS1
    datapar5['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar5['Mdm1']=Mphi1
        datapar5['Mdm2']=Mphi2
        datapar5['laS1']=LAS1
        datapar5['laS2']=LAS2
        datapar5['muSS1']=MUSS1
        #
        writeinputf('data5.dat',datapar5)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main5 data5.dat > output5.dat")
        aa=subprocess.getoutput("grep Omega_1 output5.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output5.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output5.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output5.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output5.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output5.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output5.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output5.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output5.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output5.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output5.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist5.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos5 = np.asarray(newlist5)
    np.savetxt('proceso5.txt',datos5)

@ray.remote
def proceso6():
    newlist6=[ ]
    datapar6={"la41": 0.0, "la42":0.0, "la412":0.00, "laS1":0.00, "laS2":0.00, "la31":0.0, "la32": 0.0, "Mdm1": 0.0, "Mdm2": 0.0, "muSS1": 0.0, "muSS2": 0.0}

    LA41=0.0
    LA42=0.0
    LA412=0.0
    LA31=0.00
    LA32=0.0
    LAS1=0.0
    LAS2=0.0
    MUSS1=0.0
    MUSS2=0.00


    datapar6['la41']=LA41
    datapar6['la42']=LA42
    datapar6['la412']=LA412
    datapar6['la31']=LA31
    datapar6['la32']=LA32
    datapar6['laS1']=LAS1
    datapar6['laS2']=LAS2
    datapar6['muSS1']=MUSS1
    datapar6['muSS2']=MUSS2

    for irun in range(0,10000):
        omega1=0.0
        omega2=0.0
        Mphi1=np.random.uniform(40,2000)
        Mphi2=np.random.uniform(1.0,2.0)*Mphi1
        LAS1=10**(np.random.uniform(-4,0))
        LAS2=10**(np.random.uniform(-3,0))
        MUSS1=10**(np.random.uniform(2,4))
        #divisionmasas=Mphi2/Mphi1
        # writing data.dat input file for micromegas
        datapar6['Mdm1']=Mphi1
        datapar6['Mdm2']=Mphi2
        datapar6['laS1']=LAS1
        datapar6['laS2']=LAS2
        datapar6['muSS1']=MUSS1
        #
        writeinputf('data6.dat',datapar6)

        # running micromegas and extracting the datas
        subprocess.getoutput("./main6 data6.dat > output6.dat")
        aa=subprocess.getoutput("grep Omega_1 output6.dat | awk -F'=' '{print $2}'")
        bb=subprocess.getoutput("grep Omega_2 output6.dat | awk -F'=' '{print $2}'")
        cc=subprocess.getoutput("grep 'proton ~x1' output6.dat | awk -F' ' '{print $4}'")
        dd=subprocess.getoutput("grep 'proton ~~x2' output6.dat | awk -F' ' '{print $4}'")
        ee1=subprocess.getoutput("grep vs1100F output6.dat | awk -F'=' '{print $2}'")
        ff=subprocess.getoutput("grep vs1120F output6.dat | awk -F'=' '{print $2}'")
        gg=subprocess.getoutput("grep vs1122F output6.dat | awk -F'=' '{print $2}'")
        hh=subprocess.getoutput("grep vs1112F output6.dat | awk -F'=' '{print $2}'")
        ii=subprocess.getoutput("grep vs1222F output6.dat | awk -F'=' '{print $2}'")
        jj=subprocess.getoutput("grep vs1220F output6.dat | awk -F'=' '{print $2}'")
        kk=subprocess.getoutput("grep vs2210F output6.dat | awk -F'=' '{print $2}'")
        sigmaSI1=float(cc)
        sigmaSI2=float(dd)
        omega1=float(aa)
        omega2=float(bb)
        omega=omega1+omega2
        vs1100=float(ee1)
        vs1120=float(ff)
        vs1122=float(gg)
        vs1112=float(hh)
        vs1222=float(ii)
        vs1220=float(jj)
        vs1022=float(kk)
        sigma1barra=vs1100+(0.5*vs1120)+vs1122+vs1112+vs1222+(0.5*vs1220)+(0.5*vs1022)
        semi1=(0.5*(vs1120+vs1220+vs1022))/sigma1barra
        newlist6.append([Mphi1,Mphi2,omega1,omega2,omega,sigmaSI1,sigmaSI2,MUSS1,MUSS2,LAS1,LAS2,LA41,LA42,LA412,LA31,LA32,semi1])

    datos6 = np.asarray(newlist6)
    np.savetxt('proceso6.txt',datos6)

ray.get([proceso1.remote(), proceso2.remote(),proceso3.remote(),proceso4.remote(),proceso5.remote(),proceso6.remote()])
