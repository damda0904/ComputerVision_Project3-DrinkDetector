# Drink Detector
>2020년 하반기 Computer Vision 수업 기말 프로젝트

기말 프로젝트의 주제는 tensorflow를 활용하여 모델을 만들고, Image Detection을 활용한 특정 서비스를 개발하는 것이었다. 당시 '시각장애인 시점에서 바라본 음료 코너'라는 글과 함께 올라온 사진이 굉장히 충격이었는데, 마침 주제와 적합한 부분이 있어 주제로 선정하게 되었다.


![201906121483734269_32](https://user-images.githubusercontent.com/67117391/107640919-4d337e00-6cb6-11eb-9d31-c0121fbbbdce.jpg)

>음료 위에 쓰인 점자는 모두 '탄산' 혹은 '음료'라고만 적혀있을 뿐이라고 한다



# 서비스 동작 설명
편의점에는 수많은 음료들이 있지만, 학습시킬 자료 사진을 짧은 시간 안에 직접 촬영해야 했기 때문에 4가지 음료를 선정하였다.

- 코카콜라
- 칠성 사이다
- 데미소다 사과맛
- 데자와

카메라에 음료를 인식시키면 해당 음료 이름을 음성으로 알려준다.
음성은 **네이버 클로바 더빙** 서비스로 만들었다.
>https://clovadubbing.naver.com/mypage




![캡처](https://user-images.githubusercontent.com/67117391/107640956-54f32280-6cb6-11eb-93fd-ecc994cb0fa8.PNG)
