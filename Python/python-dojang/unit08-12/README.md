# unit 08 ~ 12

## unit 08

표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때 합격이라고 정했습니다(한 과목이라도 조건에 만족하지 않으면 불합격). 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

## unit 09

출력

```{.no-highlight}
'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.
```

## unit 10

표준 입력으로 정수가 입력됩니다. 시작하는 숫자는 -10, 끝나는 숫자는 10이며 입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만들고, 해당 튜플을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

## unit 11

### unit 11-1

표준 입력으로 문자열 두 개가 각 줄에 입력됩니다(문자열의 길이는 정해져 있지 않음). 첫 번째 문자열에서 인덱스가 홀수인 문자와 두 번째 문자열에서 인덱스가 짝수인 문자를 연결하여 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 연결 순서는 첫 번째 문자열, 두 번째 문자열 순입니다. 그리고 0은 짝수로 처리합니다.

input

```{.no-highlight}
python
python
```

output

```{.no-highlight}
yhnpto
```

input

```{.no-highlight}
apple
strawberry
```

output

```{.no-highlight}
plsrwer
```

### unit 11-2

표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 리스트 x에 저장됩니다(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음). 다음 소스 코드를 완성하여 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 만드세요.

input

```{.no-highlight}
1 2 3 4 5 6 7 8 9 10
```

output

```{.no-highlight}
('1', '2', '3', '4', '5')
```

input

```{.no-highlight}
oven bat pony total leak wreck curl crop space navy loss knee
```

output

```{.no-highlight}
('oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl')
```

## unit 12

표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.

input

```{.no-highlight}
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
```

output

```{.no-highlight}
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
```

input

```{.no-highlight}
health mana melee attack_speed magic_resistance
573.6 308.8 600 0.625 35.7
```

output

```{.no-highlight}
{'health': 573.6, 'mana': 308.8, 'melee': 600.0, 'attack_speed': 0.625, 'magic_resistance': 35.7}
```