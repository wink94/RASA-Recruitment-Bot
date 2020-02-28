## welcome
* greet
  - utter_designation_list

## ASE impl
* ASE_impl
  - utter_ASE_impl
  
# ASE impl happy path
* greet
  - utter_designation_list
* ASE_impl
  - utter_ASE_impl
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
* goodbye
   - utter_goodbye
   
# ASE impl reject friend refer path
* greet
  - utter_designation_list
* ASE_impl
  - utter_ASE_impl
* trigger_reject
  - utter_refer_friend
* friend_ref_T
  - refer_friend_form
  - form{"name":"refer_friend_form"} 
  - form{"name": null}
* goodbye
   - utter_goodbye
 
# ASE impl reject friend refer path
* greet
  - utter_designation_list
* ASE_impl
  - utter_ASE_impl
* trigger_reject
  - utter_refer_friend
* friend_ref_T
  - refer_friend_form
  - form{"name":"refer_friend_form"} 
  - form{"name": null}
* goodbye
   - utter_goodbye 

# ASE impl reject friend refer reject path
* greet
  - utter_designation_list
* ASE_impl
  - utter_ASE_impl
* trigger_reject
  - utter_refer_friend
* goodbye
   - utter_goodbye 

## ASE DA
* ASE_DA
  - utter_ASE_DA
  
# ASE DA happy path
* greet
  - utter_designation_list
* ASE_impl
  - utter_ASE_impl
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
* goodbye
   - utter_goodbye
  
## ABSE
* ABSE
  - utter_ABSE
  
## APM
* APM
  - utter_APM
  
## ASYSE_impl
* ASYSE_impl
  - utter_ASYSE_impl
  

## user detail form
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  
## not apply for job
* trigger_reject
  - utter_refer_friend

## friends detail form
* friend_ref_T
  - refer_friend_form
  - form{"name":"refer_friend_form"} 
  - form{"name": null}

## reselect
* trigger_back
 - utter_designation_list
 
## say goodbye
* goodbye
   - utter_goodbye
   
## say goodbye no friend refer
* friend_ref_F
   - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
