# Chat Sentiment Analysis Service
<img src="https://www.elclick.news/wp-content/uploads/2019/08/chat-online.jpg" width="650" height="325" />

# Description
This is a **Flask - Api Creation** project for *Ironhack*.

The purpose of the project is to:
1) Create an API in flask that insert text messages in a database of MongoDB
2) Extract sentiment metrics from text interactions, through the analysis conversations from a chat messaging app, using NTLK Sentiment Analysis

# User and Chat Endpoints
## Create Username
` /user/create/<username> `

If the user name already exists, it will not be entered into the database.

## Create a Chat
`/chat/create/<chatname>`

This URL extension returns a json with the chat id in mongodb and the chat name. If you don't insert the url correctly among other things, it will return an error. Also, if the chat name already exists, it won't let you enter it again.
## Add user to Chat
`/chat/<chatname>/adduser/<user>`

The user can only be added to a chat if both the user and the chat exist previously.
## Add messages to chat 
`/chat/<chatname>/user/<username>/addmessage/<message>`

Esta extensión sirve para añadir un mensaje de un usuario a un chat. Solo se podrá insertar si el usuario y el chat existen en la base de datos.

## Show all content from chat 
`/chat/<chatname>/list`

Al introducir esta extensión, devuelve un json con el nombre del chat y todos los mensajes enviados por el mismo. El chat debe existir previamente en la base de datos, si no devolverá un error.

## Summary 
<img src="https://camo.githubusercontent.com/2cb404bc517c840be092019f1807d2165c2f373f/68747470733a2f2f6d65726d6169642e696e6b2f696d672f65794a6a6232526c496a6f695932786863334e456157466e636d4674584734674943416749434244614746305358526c625341386643307449454e76626e5a6c636e4e6864476c7662694136494677695932397564474670626e4e63496c787549434167494341675132686864456c305a573067504877744c5342566332567949446f6758434a6f59584d676332567564467769584734674943416749434244623235325a584a7a5958527062323467504877744c5342566332567949446f6758434a706379427759584a304947396d58434a63626941674943416749474e7359584e7a49454e6f5958524a644756746531787549434167494341674943416749437450596d706c5933524a5a434263496c39705a467769584734674943416749434167494341674b314e30636d6c755a7942745a584e7a5957646c5833526c654852636269416749434167494341674943417254324a715a574e305357516764584e6c636c787549434167494341674943416749437450596d706c5933524a5a43426a623235325a584a7a5958527062323563626941674943416749483163626941674943416749474e7359584e7a49454e76626e5a6c636e4e6864476c76626e74636269416749434167494341674943417254324a715a574e305357516758434a6661575263496c78754943416749434167494341674943745464484a70626d6367626d46745a56787549434167494341674943416749437442636e4a6865547850596d706c5933524a5a44346764584e6c636e4e63626941674943416749483163626941674943416749474e7359584e7a4946567a5a584a37584734674943416749434167494341674b303969616d566a64456c6b4946776958326c6b58434a6362694167494341674943416749434172553352796157356e494735686257566362694167494341674948316362694973496d316c636d3168615751694f6e73696447686c625755694f694a6b5a575a6864577830496e3073496e56775a4746305a55566b61585276636949365a6d4673633256392f" width="300" height="325" />


# Sentiment Analysis
`/chat/<conversation_id>/sentiment`

    - Purpose: Analyze messages from chat_id. Use NLTK sentiment analysis package for this task
    - Returns: json with all sentiments from messages in the chat ​

`/user/<user_id>/recommend`
    
    - Purpose: Recommend friend to this user based on chat contents
    - Returns: json array with top 3 similar users



 