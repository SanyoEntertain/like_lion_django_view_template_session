### 템플릿 태그 정리

참고 자료: https://docs.djangoproject.com/en/5.2/ref/templates/builtins/


comment: {% comment %} ~ {% endcomment %} -> 안에 있는 것 무시. 주석과 비슷..

if...endif: 이 태그 안에서 if 문이 동작.
for...endfor: 이 태그 안에서 for문 동작.
firstof: {% firstof val1 val2 val3%} 일 때, 비어있지 않은 첫번째 값을 받아온다.

for ...empty: for와 endfor태그 안에 empty 태그가 있을 수 있다. 이전에 출력, 혹은 리턴된 것이 없다면 실행된다.
값이 없을 때 뭐라도 표시할 때 사용하는 듯하다.

ifchanged-endifchanged: 어떻게 동작하는지는 모르겠지만 이 안에 있는 태그, 값이 변경될 경우에만 실행된다. event 처럼 동작하는지는 모르겠다.

include: {% include template_name %}
