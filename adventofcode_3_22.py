from string import ascii_lowercase, ascii_uppercase

INPUT = '''
LHLRlCCvCLVgHPfCHtVjBGrBDNzWFBsBGBfscGsD
nQwbnwwpbrJBrNWB
hmnSdSdQpTpdnlPdvddPNglLjH
RZhwpDsNqVmQClwl
TLJfLTPqcvTrvvLMLMlVzzvVVQQtmQCmtzmV
MJjccdfTMcbqjNSRSZsSDZ
LLrNNqCTCwLTttwcNctqFGmRBSBjzjbSzbBbjNbzjB
GnhhZQPDGdldgQmQSjpzjzQssb
gDJZPMnPnhlhJWhZntLCLcTqVMLrGVtMfM
rrBgDBGnVnffDnfQQqngJhhSRQvhhCRRRSZbRpRzwQ
NtLmcHPHMHHssFJphZpbhwpNRbbC
LJPHlmdJDgrrqrnl
nJhrcNnfrFwNhPdMQSgZSCMjQn
LjqGWsGWllRRlHVsqGGWsZZSSHQgPmHZZSPvdPCmvQ
zqqVTWjqBsTJprNbppFb
zSMgWzlgFSWFcGZlCZGlrrTc
spnQHdQmHddNmpWrpWcChccTWc
BsRsnmBQdNWsvRPzbzbLzDVSPSbVLM
lDfbffptlrJZTBJHjjBWjT
LcwwgQLgzvztwtMQGCMVCHWmnmjWnGhFHnZjmZhjhT
sCqtzsswCgccbSqrDSqbNNfN
snnnjwRRwGSSnVmhhVMhGFbgQgbzFFPPgQQmPbbgQd
qCrccvcDDcvqDZlCcrcfQNQFdsbgWzFfQddQQPgQ
ZcrvrBqBTCZnBBswjwpSRs
qSczBfBcjMZMfctsmsGmFJsmQQcQCr
wPhTLNVNGLNdGHPHwlQsnrnmnrQvHFFHQn
dLdwbNLRdgGbgTjZfDbqDWjftSzW
rZwlrtRtNtlHqVBtdqQgdq
fbwzpPwbhJzpwfTSHgdgqcJVcBjHvHdJ
LLPbhzPpTTbTshfGhPwSFWnNmMrrZZmNmZDmWNCCZs
tMHgMWMQWgFJTHsWMvJrVdlmvlSvdvlpvG
RNfZZfRttBtdlZlmmmplSS
DzzNDDRwnwwbLnMFtsMntQFM
qHqBMNqgMwHMbnGStHSbndnt
PwWZPjpfsDsDsPfPfjdbSvbWhdFSbFGSWFtr
wfpjpJcfVsspzZRRszDpwcRggLTQQBLqNqcqcggLCgNmlq
TmmFjtvFdDGjdFFJjFRDLNLHGBVcqgLcLgVBLqgV
WbWSPSwQCWrWQSrCbwNVlLlBZLBvLlvZVqPl
SfwbhrwQQbbMwCwWCrbwJRvptJfjDTDRvzTttRjp
jzqSMszqsbVVMVMgWhWCgMrpGgpB
wrwLcFQmPlFFlwLZmFGTfPvWGfPvhWWWvGgf
wRZtHFHmzNDHSqrs
NprlCgrrnrNCjplSCtljpFrFZLzzgwmVgBzBZZPwzBPQBwVL
HsDMvHTDfsfQZfZzmPWL
JcPsDGTqcTqSdrSCtnCt
cFcmfmJFtFmtlTNtLlCWTT
QPQzjRRsVsQqBqwlTlNBpLNSWDpN
QblgzRPgbgQsVvgPVQhgQqjvMnJfccnZddcGGfrFJMFGGF
PWbWmFFnPFPWbDVVmmDHDFGdGhTQdLdnTZQZZcGSGGdQ
ClzjNBlBJvlsBdcPLZdLPQjLQZ
vJMBpBzzzfNCCzCffJlzgMWDWwPDtVtmVHPMwVHD
bJjWzWFlTMjjSNBrRcBrZR
mwnwqPwnGQPCqmJmPQJPCVNcRZBRRrrNrmrcVpSrRf
PGvQQGPqvhWFWlJbDv
PNPrdmPGRJlZCrCJlGQzjRFLpFRppjgppgcj
DwfVnssbVnSWShDwsnnhBLFjFgjFBzDBjHDLpHDj
vSsMgbsTfTwwfMffnTvgNNCmrPJtCNrJrCrrtvGm
cRnRplCzccVcrwcnppVVzRCNhfhgChNJfPgHJdHDNtNCtP
WFmbLMZdLBqfJNbPTfttDD
BdMWdQsGsSsrpzrswr
llhhZzSLqlzwRrffzwzT
GvBbNjHbjjTGGHHFcsFvfRrtJQPvtRfwwfrPJD
HGbcbTTjHFNpppmLnSdplWqZ
FhwFbPwsvtRgVCgvMT
HJVHdHBWdBQSSSQnqSQLqZHtcCctppgBtRrgtMCgTprRMM
QNzZLVSLLLDGPPzPmbFs
VdTHmWCVZDTPBBWBQBFQQg
MzjMjzCjJsbJhhPz
crfGGLwwLGrtrvCtdTmdDH
wRLvLmGQLwFPBRmnLCLmGQTzNNqVNZMMVzzQbzVbNZpMVb
jsgJWjdHghsglHtWsjSfHzVNqzfpCCzqDpzDrVVrrD
jJtWWsWhtSHsSSgchthHcjHCvcFCRvwvvTTFBGvBmmGLnL
LpjWLNqWpwRWMqLRGjwJlStgbtrVgHFrGllDDrVH
SQmmTcZZvSZBTmTSzhPTddbVDhHllgFCDHtrDHgDVVDr
PzTTvznBncnfTmTTQcPdmzzMqWNfqwRLpWJsNfwLJjsSwJ
lsGdGwBsflGrfsHvHwQLdFrmPhDhCFhhjWCVmhDzmbmPhC
qtMSNNZZMpcnVzmVbCqjWjzB
ZZcgRJpBtTMNnntncwgQQdfGHHHlsQffLH
jBBtjjqfnwStBSrVVFwSVVvvWzHmcWvWbvPmPbWrbMRM
GTdNDlpJhlCvPbHgcDmgDH
JZQdQhNldLdTpGdJGdNCpLZdSBnnBFfHHswqqjffZsqsFjns
phJhDPQLDSJvpHhvDJhfrFQVRrnsslrgwrVrrRjg
mWNWqZWWZBMdCGMNCdWmWCNCsnVFTRsVnZFlsrlFwFgVsgjr
dWdjttGmNCBchJfhHvhPtvJt
CSFSFdfCzJhtSCHQFjQHQWFHRNHG
wnbrgZnwZgDLsLbwsLrsrNWQNjPZHHvPPQHNqHHvqB
LbmTLDsgggQmzmCCppdtSJtM
SzSSchCdZgHbwHSZ
GsMMmslnsfmNGNNNVVtZWdwbqQbpgWjjgWZjQm
DvlMtflGGVGthhzdvLvhrTcc
dvfVNqHlQfGRcjDczlCDnC
PsPsStLprtTTFSTLmhSVSFSsCzRRjzDnMJDCMWWDjMnMnpjW
hBFPhSBFttBhStLwmsPTtPsFHZNGfQgdgdZbdqZwdgNVvwvH
rhjcChdgjdCrjLjLLSLmLFMmFtNnnbQNNNPMbbmtQF
lwWRZDlsWzrbbQpN
rTRqsqDRRRsDRVrqDgBCdCVShjCBHchjdh
PsspltlPsmTsmbmfTPSTTCGjhJJjCnpqJJNhhJwNJh
BdrLVvgQLQVLHRZGnqRhRNdwNC
WrFVHDgDQFHVLVVDFQMLltmPsssPztwsPTzsWcmc
CBvvSzFGSGGWfFZpcHqjvjcvcqccJq
bRQwgbbhrRhdwmQbWtdjnJHqVJccJqgHVJHJcl
RRmbPrNRRPLLtmbQmbNwddCTSTzBSDBDSMFTBSSPZFFW
cppsSgNrSgwrGRdHRrwd
LzqqmCLCLWQvCzmzZwHnZZHSwvwnlDlS
hzFqFLLLFtSNVsFF
zpZcZZZdppzDLWDtJGgfGbTGGJTGcc
qhvNSClCShRrRBBWTQfgBFbgtfgg
HlHqvjqmCvCvlSSHvVdsVDzjpVjMWdwLpP
qLdsfNsTHQwnSNSBNS
gFhWzrhfbmlpmZhJWrFSvRMnwwvvpBpBSpQBMv
rgWZrbmlmbzFfglgWzGggFJLccVPqLPqtPLGcPsPHcPLTd
jTTWRCCbwJJNTHrffqNnzh
DZVmDpgGBVdcMZnqfhlNHQMlNNhl
sDcpsDZBcmgdssZcnmSWCPWRSRwJWwvFLvRwWj
hWwhgQlQQgjPhFChZVdbcJ
zHsrMPNMtDDTmbcJbccmDb
znzPzrtHtHtMzqHHrsSSLwljqfgwGggjlQjQQgQBGj
JpnRtqlJsqDJJBBNNmQmgdmRNGGmvv
hTCbTwMCwVhTWdmDgDvjWD
MDhhMSwZCbbLVhbLcDSwCwZtZznlzlnqBPBpHPPlBlHJ
CtvnvqNNDchrhFVpwftmgQgpQfwS
MbdqPWGjBjMBbwlfVgdmfSfJJS
jWzbzjWWjWMMbRbMsjzBhChrNHcNqHcrNnhssnsc
LlLJSWgWllSShRmRlBLJSVBzpTHzTTJcpTHzpTTcPpGpTr
MfMqnvbvDfbFFZDfFNjsGrRppHpZGGcGrcPprz
wfNFvtwMvbnntftjfNtVmlgmStBmlBWdQQRg
GpFRRPGWqzHwdqpzqbjjgfZptBBVMSjSfBZc
TClllrnsJvDMBgcjfmtssB
NlhNNchrNJlLvClNDrzbGRqwqqqwqPPFLGdd
qFmVtvmmVvzzFtzzGzzMNNMSSTjNJlStjSfNgf
sWrPBCnCTMsTJfSM
QTLbpnRpRppnRQdRzRZqGzFFVVRz
WGGPjFvMVNjlcQJr
bslfldbgtpSmwmSNHQhLJhcwLcQrQV
gTltCsSsssPFnDzWPTMz
hhRRhQgGrHjhRsrgqznbzncZjVVJVjncjd
DSFfNTBFSDmMSTDlFbBBdccCdJJZCbZCbW
DDLmdSmTvQQgsgvGHH
dNqNgNvFnvdZHFWnZWNBTQlPTppPGlCTpBQppq
LJrtLrsLjsGvTCTpQP
mtLhjVjMhhmVMvtJmLfhFWHnngbRRdZHngnZWZ
NzdVNzqqCtCHMMZBCGBW
psjllRjFpjpbjspFmWmWnLBmMMQMmHbm
DhsTPDRTDHpsvRjdNtzJJJdhqwcdqc
VbhRbZgRHMFhQpHd
fvlqPzmzJJqJSPsWmPTNddNFHbNFGHNTHSbc
CqzlfqrCnbrBZjBr
SNSrDZFHnTqFsFddsCmsMC
ctVthlGjfhGljcCJmcqMCqcqBB
VtjvtjhhPPtWqVPLjvqjLVNRppRTvNSnbnZRZTHRnpTD
fzsBSsNBMNMszNGGJvgjjPggzjdFPgpJ
bmrVVVrmRrrvRmwvqlbHTDgwdLFjQPJPFddwJPFggj
HHHrZqhqbTMcZBCZfvcN
tzsJsnsmBzlVqjssZZrg
MQZHfNCffpMfpGSpPvpfCGCTTVwFTlwrggjSgqFjVjTwwg
NfMGGGPZpvLDvLCGGfQHMpZRDRWchRRtBBzmJnmzmnBznb
BSRBjtNjZrsjRjjNsVBjbrMwCgGCCwCdHrlcdccGcH
DJTTJLpFnFLdJJqPLTWqLTpwHzCGccCzvvcHwMvWzggCMC
PmpTTdndmmLqfLTTLDqJVBssbbStVmjjSsZNsBZm
ddCnZvCDSgghFhbbmFVQ
JzlMcJTMMPPfJJfsMsjWlHVhLbQVlFWmHbbb
BPwwsPfsqszfFqppwTsqzpntDSnCBnDRZrSZdnDdtvZD
SllzzPplWldwLGlzbtPZZjVScnnNSjnNsqNqsc
BrCfFDJFDHBhJCChQFhCCBDcTnNVpZZcNcvQTcjvvcTcZV
RCmFHJDJhCmBmRCgDCFRpmGbWWbLPlbMWzzGttzgLMbt
vGTfsZnfvfzTjsnfzTJlwqQjwmCqqMFjFFQMlq
LHtHRVLRLNtWcmVbRrPbRcwgQwgwMwClwClwrgFpwqpw
VDPtbVLBmLbLbDDNnnnzJJfJfBfvSGBn
lpPCRVVQppzHlZgzglgF
rtfttLdLdscmGtzngPHHFHFH
LPLLhfhbTDLmPdcrcWdTcDSjjRqwwbqpRwNBNpBwjQwR
dWQfCJrwvQCfFqNwRbbzVbVVLGTR
ZpZshPMzBjGjtVMN
phpSlSlDlcZpcZPrdHCFzFzFWFDWQH
tfMMZhjLlChsdsds
PHQRMHRwpRPBMvWvPRBpPdWDslGrbscTlTGcCsGddG
FqPSvHPHPBzQRBBwwRJfVtgjzntMntjJLMtJ
VBwJvwVwNbVRdPwMgWggGMgH
jDhqflDDhrqshNhdgPGHphLg
FltsrtcFrclrNqDfqmzQJQQRBzBCvCFvBR
RZsSSJDJZLDWnGDMLD
ClbnlfmpNtmgbtmMqWdjNGjLQjLqLj
gcblTlVCnVmcPrvRPFRrZs
mbJcScmbDWLmSBzwjPRTfjmmRhpl
tFFFtGttdClHVMCHFMMwTpwNjGpzPpNRRzzpPN
gCCdvZCVHsFvJnnDSglSglDn
dSndnRRvVSpLSphfqvTgWqrzqvvw
PBFQbQbDhGfjTTFzqG
tPmCJMtDDNcMVdhhVc
QVRVHCQRmdTRqrZFCWrLZNZFbb
ncncsPnhslBRSSSbFhtbZDLMbLbtLb
lvflPcfPSsPzlJlPlcPBfHJQwRwHmqdVpRGGGdQmww
GTCGMCcGdgRnnbbbMLwmMz
DQFZzllWDDLwDJLnJpnp
qBVrNNlZfFNlWlWqfRzhgvhCqHRdCGGSvc
ZnMnGbLZfJcBcLTgWF
dHJjdzqssHHNJwCHpHtDccvtBTtvccWWrrTWSg
CmlqCNzCzHlmdsqzNzRhMhZRbZMPmRfRJQPb
LsLLrFLcFjrtmZhhmhHGhJGGhH
ffvbsbWpSBSSCCQbsSBSwwJHHvhZHHGdGVGlMlTVdZlT
pSzWNPSfCwWNPBfsFqtFLtsqRzqFgj
hwwpvjVppGpwWGLrcPjrbrrdbjdL
FBqFFMFHHsHssNHtslqtFmldnnLrPhMnccrnMzZnbLgPLz
mJBSstlJQpwGSVhC
cgJDVWsrWggpcHhMzwwPnQMWMm
SZGBjdBqBBjGjjqNGfGNNHPnRSQFzhnwmnQzQnPHMR
bjjCZddjZbZBCtLhCZhftrgJglcTlJgvTllJvDVDLg
QpRJpCFdpqTQcqSTBBGBZVjZjVjFvwVB
nnnWfnHhPDlDnlLwGjBBbVVZGbCGbP
LhhLMLMrMWMrCprTqpJQpz
dqGGZJdZbTTMFFTGJFFbMdnCHSdWcmNmcCdWSggfSW
QsjjtrzLrQwDPjrQLrCfSSnmCmHWlCgmzlNl
PQpQPjQPsBstLBPttDrjBwTZMFMZFvJFJhMhnMJqpTJJ
JMLrSvHJdJvvJfrHMJRfWzWDFPwCcWqRRRcq
ljZsZTmmtTBlpTlTjQZCtNFPVqDRwWwWWVPcDRVpFRDz
mBgQgNNTNvrvJSvgCb
DWbWtzWDfDffbsMbZMffDDLncnnCJmLVsJJJnhgcngLs
TjgNGSBRTRTQrFRjFGBVLwLnnNncCLLCCcmhPC
GgGjvgddvvWqqfdZftWH
zMmsQlMfQQMhjsmjfsmHlhncRRZnRRRJRvZWWnhccdRC
BptFtDSSrTrpgtgqqgtZtvVVdVvccVnJdVnG
qpgPqBLDNTgqBrSLpDBMJfjzmbJMHjLMfjslzH
DPgLgPhfNDRqhDFDsBTtrrrdbbztCbtf
MjGSScGVGSlJjbbrtTvdzsTq
JJwJGWMZwMlWnFFgqNQFpF
WRGDHmGqWHlrmtVVVRVqpNZvZvvvTNPMPjbPdM
BwhBwsnzwhzSfCfswFvpvTzTdpMpjvPMZNTb
LFFQgnbfChSFBhFnftRRLrttDmmRJHtlGH
MhqhRHmDdRlRlGnfZbJVsNNZDnNb
QwvzgtwvFpmjwzLjFLJZrsZbPfPZbsVpfPsb
gvjTzBLztLTjwFjtgLTgtzwdWRqdqRTMSWcWTmWlqdhHHm
ZfzzfmhdpNLNBDDsFfQVCDggfV
HPFjljSnHrqVDgtgQgQMqC
rGnSJHvjSwGzwFhGZG
HqmHRDprrNTZTMbh
CJvzQRQVQCgNzZbzgMNd
vPCvFPcfQFlSJBcfRcPHmDGqWGDqpGtjjtGGHl
wcfpJVHfJBffBBGWRprNRWWWNdhv
DzMzMPqjDnjgCMZPZjzjCjChGdvvbhNdSvrhNWSNqWRRdS
jjCTtnMTDsMBtLRQwwQlFV
JqGnVqCTpDVCTnNLgmPzdgjcGmRg
HrSBJSHblsJthsBBSBhMsrzmdNRccjLzgcLmjgPPjlLL
HSwSttbswWJrbrSWppvVqvvnQVppQQ
JDCHssRTTwcRJDcnCDzRHsHNPZGBtPzFPSPttZSZGBqPBZ
vWhLmTlfrhFqGWSNQNqF
vpMhhpfvmTfhvbLhhgvmgvvlCCJCCMnDnDCnsjRMVDMDswCC
ZgjdlmlmmlJgHJlbZrSDrnrMrmLLDFprmp
TvqdTtdctvvDrGGSDn
CWPBhtWqPPwcdVwlNJfVVNNbbb
vgmrrwlPPrwPBPtmvFcMMrsMSJHscJcMSHDH
TWdLnZjCLGLMQLHBLS
jqVTTZqjdTVjNFNPqBvgvBNl
jmcgMzsmjmfvJwFpFfRWZRWp
drdSldTmCmTDCNCtbRRWqRwtttFZpZWZqw
NLCVLNLTbbTrQNQDvnzschgghnmnHQcH
sRVhVQDVDQRRMQhsqtRRNzqzbNzRqNGp
WdjCLHLjdFnCCnjnFnLHHmPmNJbztJJpprBpbGzbpJbqGWtB
CCFFCnFjdnjCTHmCLTLLCnFnQVhQQVDMhQQVgZZNVVDDsTVh
cGLzZgfzcNNzzRZvjvRmVDmmqCCDSdVVChVnDf
QstsPlWHQlWhMMtpsbtpQtlpDqBVqPSCSVnTTqmVdDVDVdBV
stptQFJrHptlQsFJMHtHhFbvNwvjLGvvNgzgjcwczzJcNJ
SQHCrCFPJZcnWrqn
vfJvJjfGGDggqZGcWD
pjLpRwzhRFtHdMQJ
HNSHNDvnvdffDNfqdZfdStcFFMGmmrRBcmFcrMrqrWFB
VblwzwhwPLlCGGzgzhmFjbjFrMFrjFBmbcrM
hlVPTCCQCCzVlPzhGgPVJCpHtdtSpQSZNNfnZdSSdnSD
cBVmfwqwmWggTRmQzTQl
CDnnHjSDPLCSCLHLHCHNCDFgwJljFQRRhlglbzJFQQhl
GptHLtNGHtCHSnCMtGWdcsqqWwMcqvdsVwfd
HsMFNRNWnbWfZLzWzQ
PqrpjqNdjjhPcdbpvmfzfbffbzmv
GjhhcPjPccVrqcPCldCjssHNnTnNttRwwVMTHMnV
jjCcBswcfnwgpPFPwFFGSFSwFb
VvmVhVvRRQqttRtQDLzLhqRlrBFMWrGPBSMSZSMFqBWZZP
mvQmLRvJtBJVnTcJCjsjsdgp
qgqvPbdMDMMPwpbLFGwtNlNF
TTQmdJTnSllFGtJNtw
CSSHmQHfmVcHjQmSvPBdBDDWMVhMhRMB
WCvQNZdhCDnnPfQPfTzjHcppsHjpsSjHNS
mFMgMBlMmBqHjjBfTjHzBc
grJbrqfqMVFJrlJrtCtvhPPQdnvnnvnwdW
FdQQJRdfSSfrJsRZfFsRSvtDBmDHGtGqbgvnmbDnvDGq
lcMzjCPTVtMqgWWGqn
VpLjcVPczhzznPLcPhTwFQFRZNfFNrNZFpZNsZJR
VWgJhmdDdJDdVPggPSTSTWvvfRzfFfFbNb
jCQtnpGQrHMctnpzRbFfgSwHvgwfwv
ntcMcqLMcQccQLgjBPLdhZDVlJPVdDLJ
RnPnwtqHnJthjLMcWWncMn
msdCrCdNpBBsCrlNTpNBDNGzcLchQjFQzccQLQpzLzWtFS
sTbdTBNrTCTTBCNBlVbwgVPJHtPgPvqgff
QmBsmpmcZQNqPqVnPFVpGh
gDDMDLMJgHfJwJMzfTfdGLhChPtvnGRPRRLFGPGv
DTlzgwfDrrrMWlncbscNnlSW
tBwvGHFttrFrvRgRhCmCmwQmMg
JWbNJZjzfbVjWjBhqfmSnhqCqgnQ
ZZJJJbclzJcsTPdvTTPTBFtHDF
LszmFTFpTmszLrpqSmFpzcvQjtQjvLJgJtcBjgtJjj
VHNwwNCVCChddfwHlWdnlnGRQPcQjRvMWBJJtMMWcvPJMM
nGHNVHhnfnHDNhCfdhNNlwHvmpDrZDmpzmbZSZFsmmbqrrsz
'''

def construct_score():
    score = {}
    for num, letter in enumerate(ascii_lowercase, 1):
        score[letter] = num
    for num, letter in enumerate(ascii_uppercase, 27):
        score[letter] = num
    return score
        
def get_dupe(part_1, part_2):
    for c in part_1:
        if c in part_2:
            return c

def get_dupe_2(part_1, part_2, part_3):
    for c in part_1:
        if c in part_2 and c in part_3:
            return c
               

if __name__ == "__main__":
    sacks = INPUT.split('\n')[1:-1]
    value = construct_score()
    score = 0
    #for sack in sacks:
    #    if sack:
    #        split = int(len(sack) / 2)
    #        part_1 = sack[ : split]
    #        part_2 = sack[ split: ]
    #        score += value[get_dupe(part_1, part_2)]

    sacks_1 = [ sacks[i:i+3] for i in range(0, len(sacks), 3)]
    for sack in sacks_1:
        score += value[ get_dupe_2(sack[0], sack[1], sack[2]) ]
    
    print(score)
    