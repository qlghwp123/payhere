# 목차
* 기능
* 환경
* 미구현
* 후기

<br>

## 기능

* User
  * 회원가입
    * UserCreationForm 을 상속받은 CustomUserCreationForm 을 활용
  * 로그인, 로그아웃
    * 로그인 Form 은 AuthenticationForm 을 활용
    * 로그인/로그아웃은 ```django.contrib.auth``` 의 login, logout 메소드를 활용 
* Article
  * 생성 및 수정
    * ArticleForm 을 활용
  * 삭제
  * 목록 조회
  * 세부내역 조회
  * 복제
    * pk 값을 url 통해 가져와서 똑같은 article 객체를 만들고 DB 에 저장
* shorteners
  * 단축 URL 생성
    * ```string.ascii_letters``` 를 통해 알파벳 대소문자 중 랜덤하게 10개를 뽑고
    * 해당 문자열을 현재 url 과 합친 다음 Link 객체 생성
  * 단축 URL redirect
    * URL 로 부터 넘어온 랜덤으로 만들어진 문자열을 ```/s/``` 와 연결해서
    * 해당 데이터를 기반으로 Link 객체를 찾아서 원본 URL 로 redirect 
* 접근 제한
  * 데코레이터
    * login_required 를 활용

<br>

## 환경

* Django(3.2.13)
* MySQL Server(5.7.9)

<br>

## 미구현

* JWT 토큰 발행해서 인증 제어 실패

<br>

## 후기

* DRF 와 JS에 미숙해서 순수 Django 기능을 활용해서 구현했다.
* 해당 과제 의도와 맞지 않는 방향으로 구현해서 아쉽다.
* 내가 시도한 방법에서 JWT 를 활용할 수 있는 방법을 찾아봐야겠다.
