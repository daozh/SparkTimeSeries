import mathimport globimport timedef median(l):    half = len(l) // 2    for ind,elm in enumerate(l):        l.pop(ind)        l.insert(ind,math.sqrt(math.sqrt(elm)))    l.sort()    if not len(l) % 2:        return (l[half - 1] + l[half]) / 2.0    return pow(l[half],4)fpath='evfiles/2015/01/'datafiles=glob.glob(fpath+'*.txt')print datafiles[1][16:31]events=[]for fname in datafiles:    events.append(fname[16:31])eventlist=list(set(events))print len(eventlist)# event data as freq dictionaryeventdata=[]for eventtime in eventlist:    #print eventtime    freqdict=dict()    for file_name in glob.glob(fpath+eventtime+"*.txt"):        fp = open(file_name, "r")        for line in fp:            words = line.split()            tstamp = float(words[0])            freq = float(words[1])            if tstamp in freqdict:                freqlist = freqdict[tstamp]                freqlist.append(freq)                freqdict[tstamp] = freqlist            else:                freqdict[tstamp] = [freq]        fp.close()    eventdata.append([eventtime,freqdict])print len(eventdata)print eventdata[1][0]tic =time.clock()for eventfreq in eventdata:    freqdict=eventfreq[1]    #print eventfreq[0]    tstamplist = freqdict.keys()    tstamplist.sort()    medfreq={}    repath='mfresults/'    #with open(repath+eventfreq[0]+".csv","w") as fo:    for tstamp in tstamplist:        freqlist = freqdict[tstamp]        medfreq[tstamp]=median(freqlist)            #print tstamp, medfreq[tstamp], freqdict[tstamp]    #        fo.write(str(tstamp)+","+str(medfreq[tstamp])+"\n")    medfreq['max']=max(medfreq.values())    medfreq['min']=min(medfreq.values())    #print medfreq['max'],medfreq['min']toc=time.clock()print toc-tic