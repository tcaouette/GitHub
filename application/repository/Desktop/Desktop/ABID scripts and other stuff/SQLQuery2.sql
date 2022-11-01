

CREATE Procedure [dbo].[usp_stg1_LOAD_EL]
	
AS

DECLARE @SQLA nvarchar(max), @SQL1 nvarchar(max), @SQL2 nvarchar(max), @SQL3 nvarchar(max), @SQL4 nvarchar(max), @SHEET nvarchar(max), @ConnStr1 nvarchar(max)

/*if object_id('tempdb..##lndg_Autoload') is not  null
   drop table ##lndg_Autoload;  
if object_id('tempdb..#Autoloadtemp') is not  null
   drop table #Autoloadtemp;  
if object_id('tempdb..#Autoload') is not  null
   drop table #Autoload;  
if object_id('tempdb..#AutoInv') is not  null
   drop table #AutoInv;  
if object_id('tempdb..#AutoRef') is not  null
   drop table #AutoRef;  
if object_id('tempdb..#Investigational') is not  null
   drop table #Investigational;  
if object_id('tempdb..#Reference') is not  null
   drop table #Reference;  
if object_id('tempdb..#AutoAll') is not  null
   drop table #AutoAll;  */

SET @ConnStr1 ='C:\Users\u106421\Desktop\ABID_exce\abid1.xlsx';

SET @SQL1 =  
'SELECT ''';

SET @SHEET =  
'AutoImport';

SET @SQL2 =  
''' SHEET,
 cast(F1 as varchar(255)) [rowid],
 cast(F2 as varchar(255)) [sample_ID],
 cast(F3 as varchar(255)) [subj_age],
 cast(F4 as varchar(255)) [subj_sex],
 cast(F5 as varchar(255)) [sample_antibodies],
 cast(F6 as varchar(255)) [samp_type],
 cast(F7 as varchar(255)) [anticoagulant],
 cast(F8 as varchar(255)) [collect_date],
 cast(F9 as varchar(255)) [storage_temp],
 cast(F10 as varchar(255)) [enroll_date],
 cast(F11 as varchar(255)) [enrolled_by],
 cast(F12 as varchar(MAX)) [comments],
 cast(F11 as varchar(255)) [all_tests_excluded]
INTO tbl_stg1_EL
FROM OPENROWSET(''Microsoft.ACE.OLEDB.12.0'',''Excel 12.0;Database=';

SET @SQL3 = 'TypeGuessRows=0;ImportMixedTypes=Text;IMEX=1;HDR=NO'',''select * from [';

SET @SQL4 = '$A2:K20000] where F2 is not NULL and F2 <> "XXXXXXXX" and F2 <> "" '')';

SET @SQLA = @SQL1 + @SHEET + @SQL2 + @ConnStr1 +@SQL3 + @SHEET + @SQL4;

EXEC(@SQLA);

