# *************INSERT CURRENT PATH AS SYSPATH*************
import os
import sys
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(1, 'C:\\Dev\\RPA\\Common')

# *************IMPORT COMMON SCRIPTS*************
# These Scripts must be placed with CommonCaller in the same dir.
import SAP_Bridge
import pdf_to_image
import Invoice_OCR
import Utils
import smtp
# import word_to_pdf
"""
Responsibility
 Check valid parameter or not based on the business & system logic
   so that every method could check other things first
 Preprocess string args if they need to be list/dictionary/etc
"""


# *************CALLER FUNCTION MART*************
def call_sap_bridge(initiate_code, server, args):
    current_code_list = ["4_2_1", "4_2_2"]
    current_server_list = ["OED", "OEP"]
    my_logger = Utils.create_logger()

    if args is None or initiate_code is None or server is None:
        ret_str = "SAP_Bridge:1:Amount of parameters are not matched!"
        my_logger.error(ret_str)

    # 괄호 제거
    args = args.strip("[]")
    # 리스트로 변환
    if "," not in args:
        args = [args]
    else:
        args = args.split(",")

    if server not in current_server_list:
        ret_str = "SAP_Bridge:1:Wrong server name! server=" + server
        my_logger.error(ret_str)
    elif initiate_code not in current_code_list:
        ret_str = "SAP_Bridge:1:Wrong initiate code! initiate_code=" + initiate_code
        my_logger.error(ret_str)
    else:
        ret_str = SAP_Bridge.main(initiate_code, server, args)
        my_logger.info(ret_str)
    return ret_str