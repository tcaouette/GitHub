USE [NA5C]
GO
/****** Object:  StoredProcedure [dbo].[usp_stg1_LOAD__AUTOLOAD__1]    Script Date: 5/12/2020 8:00:11 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<David Kleppang>
-- Create date: <17th November 2017>
-- Description:	<Load Procedure for autoload data>
-- =============================================
ALTER PROCEDURE [dbo].[usp_stg1_LOAD__AUTOLOAD__1](@ConnStr1 nvarchar(255), @DataEntryPersonNumber tinyint, @TrialKey nvarchar(255)) as
Begin
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET DEADLOCK_PRIORITY LOW
SET NOCOUNT ON

PRINT 'Procedure: '+Object_Name(@@PROCID)+', '+cast(@ConnStr1 as char(255));

DECLARE @SQLA nvarchar(max), @SQL1 nvarchar(max), @SQL2 nvarchar(max), @SQL3 nvarchar(max), @SQL4 nvarchar(max), @SHEET nvarchar(max)

if object_id('tempdb..##lndg_Autoload') is not  null
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
   drop table #AutoAll;  


SET @SQL1 =  
'SELECT ''';

SET @SHEET =  
'Sheet1';

SET @SQL2 =  
''' SHEET,
 cast(F1 as varchar(255)) [SampleID],
 cast(F2 as varchar(255)) [DonorSampleID],
 cast(F3 as varchar(255)) [Method],
 cast(F4 as varchar(255)) [Test],
 cast(F5 as varchar(255)) [Date],
 cast(F6 as varchar(255)) [CardSerialNumber],
 cast(F7 as varchar(255)) [DonorCardSerialNumber],
 cast(F8 as varchar(255)) [OperatorInit],
 cast(F9 as varchar(255)) [Well],
 cast(F10 as varchar(255)) [Result],
 cast(F11 as varchar(MAX)) [Comment]
INTO ##lndg_Autoload
FROM OPENROWSET(''Microsoft.ACE.OLEDB.12.0'',''Excel 12.0;Database=';

SET @SQL3 = 'TypeGuessRows=0;ImportMixedTypes=Text;IMEX=1;HDR=NO'',''select * from [';

SET @SQL4 = '$A2:K20000] where F1 is not NULL and F1 <> "xxxx" and F1 <> "" '')';

SET @SQLA = @SQL1 + @SHEET + @SQL2 + @ConnStr1 +@SQL3 + @SHEET + @SQL4;

EXEC(@SQLA);

-------------------------------------  Obtain SiteCode ------------------------------------
--DECLARE @SiteCode CHAR(5) = (SELECT DISTINCT t2.sitecode FROM ##lndg_Autoload t1 
--JOIN dbo.tbl_CONFIG_Site_MANENTRY t2 
--ON LEFT(t1.SampleID,4) = t2.SiteID AND t2.TrialKey = @TrialKey);
----------------------------------------End of Obtain SiteCode-----------------------------

---------------------------------------Delete prior entries--------------------------------
-- NO DELETE ENTRIES FOR THIS TABLE
--------------------------------------End of Delete prior entries--------------------------	

------------------------------------- Insert into staging table----------------------------
INSERT INTO [dbo].[tbl_stg1__AUTOLOAD__1]
SELECT @TrialKey as Trialkey
 ,t2.Sitecode
 ,t1.[Test]
 ,@DataEntryPersonNumber as DataEntryPersonNumber
  ,GETDATE() as DateLoaded
 ,t1.[SampleID]
 ,t1.[DonorSampleID]
 ,t1.[Method]
 ,t1.[Date]
 ,t1.[CardSerialNumber]
 ,t1.[DonorCardSerialNumber]
 ,t1.[OperatorInit]
 ,t1.[Well]
 ,t1.[Result]
 ,t1.[Comment]
FROM ##lndg_Autoload t1 
JOIN dbo.tbl_CONFIG_Site_MANENTRY t2 
ON LEFT(t1.SampleID,4) = t2.SiteID 
AND t2.TrialKey = @TrialKey
WHERE t1.[SampleID] IS NOT NULL
---------------------------------End of Insert into staging table----------------------------

END
