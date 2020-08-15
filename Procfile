web: gunicorn sample_app.wsgi --log-file -



{% load static %}

<!DOCTYPE html>
<html lang="ja">
  <head>
    
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>HOME</title>
    <link href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
    <link rel="stylesheet" href="{% static 'css/reset.css' %}" />
  </head>

  <body>
    <div id="body">
      
      <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
      <div id="header" class="box_header">
        <a id="btn" class="name_service" href="">Sinapse</a>
        <input
          type="search"
          class="input_search"
          placeholder="🔍キーワード、#ハッシュタグを入力..."
        />
        <div id="btn">
          <img class="btn_headerUser" src="{% static 'images/userimages/user00.jpg' %}" alt="プロフィール画像">
        </div>
        <div class="btn_create">
          <p>✏︎ 投稿</p>
        </div>

        <div class="logout">
        <a class="signup_btn" href="{% url 'login' %}">logout</a>
        <form id="logout" method="POST" action="{% url 'logout' %}">

    
        </form>
         </div>


      </div>

    
      <!-- ▲▲▲▲▲ header ▲▲▲▲▲ -->
      <div class="posting">
        <h1>Create</h1>
        <br />
        <br />
        <button class="adding">add</button>
        <form method="POST" action="{% url 'create' %}" enctype="multipart/form-data">
            {% csrf_token %}
            Title:
            <br />
            <input type="text" name="title" />
            <br />
            <br />
            Comment:
            <br />
            <input type="text" name="comment" />
            <br />        <br />
            Url:
            <br />
            <input type="text" name="url" />
            <br />        <br />
            Thumbnail:<br />
            <input type="file" name="image" />
            <br />

        </form>

      </div>


    </div>
  </body>
 
</html>


