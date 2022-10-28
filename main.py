import os

from Utils import ScriptHelper


if __name__ == '__main__':

    def get_initial_script():
        return """DECLARE @APJCHP01 UNIQUEIDENTIFIER
DECLARE @APJCHP02 UNIQUEIDENTIFIER
select @EMEACHP03=id from PaymentCode where PaymentCode = 'EMEACHP03'"""

    def get_template():
        return """
-- #number#.  #PaymentCode# #CustomerSet#
select @CustomerSetId=id from CustomerSets where RTRIM(LTRIM(code)) = '#CustomerSet#'
IF (NOT EXISTS ( SELECT TOP 1 1 FROM PaymentCodeCustomerSet WHERE CustomerSetId = @CustomerSetId AND PaymentCodeId = #PaymentCode# ))
    BEGIN
        BEGIN TRY
            INSERT INTO [dbo].[PaymentCodeCustomerSet] ([PaymentCodeId] ,[CustomerSetId])
            SELECT #PaymentCode# as PaymentCodeId, @CustomerSetId as CustomerSetId
            PRINT 'SUCCESS: #number#. CustomerSet code: #CustomerSet# for PaymentCode: #PaymentCode# was successfully INSERTED into PaymentCodeCustomerSet table'
        END TRY
        BEGIN CATCH
            PRINT 'FAILED: #number#. CustomerSet code: #CustomerSet# for PaymentCode: #PaymentCode# was NOT INSERTED into PaymentCodeCustomerSet table due to: ' + ERROR_MESSAGE()
        END CATCH
    END
ELSE
    BEGIN
        IF (EXISTS ( SELECT TOP 1 1 FROM PaymentCodeCustomerSet WHERE CustomerSetId = @CustomerSetId  AND PaymentCodeId = #PaymentCode# ))
            PRINT 'SUCCESS: #number#. CustomerSet code: #CustomerSet# for PaymentCode: #PaymentCode# was ALREADY inserted into PaymentCodeCustomerSet table'
        ELSE
            PRINT 'FAILED: #number#. CustomerSet code: #CustomerSet# for PaymentCode: #PaymentCode# was was NOT inserted into PaymentCodeCustomerSet table'
    END
"""


    path = os.path.join("c:\DATA-SCRIPTS", "PaymentCodeCustomerSet")
    datasource_filename = "New-PayCodeCustSet-Map.csv"
    filename_export= "DEPLOY_New_PayCodeCustSet_Map_Python"
    list_data = ["#PaymentCode#", "#CustomerSet#"]

    ScriptHelper.generate_file(path=path,
        datasource_filename=datasource_filename,
        filename_export=filename_export,
        database_use_name="USE [DcStore]",
        row_list=list_data, template=get_template(),
        separator=";", script_title="DEPLOY",
        initial_script=get_initial_script())




