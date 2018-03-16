# DDAPI Documentation

**URL**: [api.digitaldemocracy.org](http://api.digitaldemocracy.org/)

To build a proper request you, the developer, will have to build a header containing your `api-key` and `email` which is the email used to request the **API key** from [api.digitaldemocracy.org](http://api.digitaldemocracy.org/)
## Available API calls

### GET Hearing Transcript by id
---
**Description**:	Returns full transcript of a hearing including video timestamps and speaker names

**Endpoint**:	**URL**/service

**Method**: `GET`

**Parameters**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**callType** = hearing\_transcript\_by_id  	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**hid** = \<Hearing id from Digital Democracy database>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/A

	Success Response:
	
		Code: 200
		Content/type: Application/json

	Error Response:
		
		Code:		400
		Reason:	Incorrect parameters
		
		Code:		401
		Reason:	Don’t have permission (api-key / email)
		
Example Request:  

	URL/service?callType=hearing_transcript_by_id&hid=15
---

### GET Hearing id
---
**Description**:	Returns first hearing ID match for a given committee, state, and date

**Endpoint**:	**URL**/service

**Method**: `GET`

callType = 
			**date** = \<date of hearing>
			**committee** = \<Committee that met during hearing>
			**state** = \<state where hearing occurred>


**Parameters**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**callType** = hearing_id   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**date** = \<date of hearing>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**committee** = \<Committee that met during hearing>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**state** = \<state where hearing occurred>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional**:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/A


	Success Response:
	
		Code: 200
		Content/type: Application/json

	Error Response:
		
		Code:		401
		Reason:	Incorrect parameters
		
		Code:		401
		Reason:	Don’t have permission (api-key / email)
		
Example Request:  

	URL/service?callType=hearing_transcript_by_id&hid=15
---
