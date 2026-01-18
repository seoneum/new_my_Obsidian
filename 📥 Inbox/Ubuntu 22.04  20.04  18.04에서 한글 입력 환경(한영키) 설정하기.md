---
title: [Ubuntu] 22.04 / 20.04 / 18.04에서 한글 입력 환경(한영키) 설정하기
source_url: https://gosury32.tistory.com/24
author:
  - "[[네온 무드]]"
published: 2024-07-24
created: 2026-01-08
description: 우분투를 처음 셋팅하면 한영키도 먹히지 않고 한글 입력이 되지 않는다. 인터넷 상에는 여러 방법들이 있지만 경험적으로도 가장 현명하다고 생각하고 18.04, 20.04, 22.04에 모두 사용 가능한 가장 간단한 방법으로 소개하겠다. (필자의 환경은 22.04지만 18.04, 20.04에서도 이 방법을 사용했었음) 1. 먼저 Setting에서 Region & Language 탭으로 이동한 후 [Manage Installed Languages]를 클릭한다. 2. 그러면 다음과 같은 팝업이 뜰 텐데 그냥 [Install]을 눌러주면 된다. 3. 알아서 필요한 파일들을 설치 중이다. 4. 재부팅해준다.reboot  5. Setting에서 Keyboard 탭으로 이동해서 [+]을 클릭 후 [Korean]을 선택..
tags:
  - "clippings"
migrated_from: CMDS/100. Inbox/140. Web_Clipper/Ubuntu 22.04  20.04  18.04에서 한글 입력 환경(한영키) 설정하기.md
updated: 2026-01-18T16:42:53
domain:
  - phil
cmds: inbox
---
> [!summary]+ 3줄 요약
> - 우분투 설치 후 한글 입력 및 한영키 설정을 위해 'Region & Language'에서 언어 팩을 설치합니다.
> - 'Keyboard' 설정에서 'Korean (Hangul)'을 추가하고 기존 영문 키보드 설정을 제거합니다.
> - 'Korean (Hangul)' 설정에서 Toggle Key를 'Alt_R' (한영키)로 설정하여 한글 입력 전환을 완료합니다.


우분투를 처음 셋팅하면 한영키도 먹히지 않고 한글 입력이 되지 않는다.

인터넷 상에는 여러 방법들이 있지만 경험적으로도 가장 현명하다고 생각하고 18.04, 20.04, 22.04에 모두 사용 가능한 가장 간단한 방법으로 소개하겠다. (필자의 환경은 22.04지만 18.04, 20.04에서도 이 방법을 사용했었음)

**1\. 먼저 Setting에서 Region & Language 탭으로 이동한 후 \[Manage Installed Languages\]를 클릭한다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdHBLI1%2FbtsINtKHYdL%2FAAAAAAAAAAAAAAAAAAAAAFEzovLL1lAVE7XPdwny0FIsdPcOjVaSga6wNulh39UQ%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DpN8AhHy%252BO6iXc7SM11AFsIrkz4Y%253D)

**2\. 그러면 다음과 같은 팝업이 뜰 텐데 그냥 \[Install\]을 눌러주면 된다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fn1Ocs%2FbtsILk2OIM8%2FAAAAAAAAAAAAAAAAAAAAAPzZGozH0v0S8TanKX0lIzS8ig8WJUnUUjQ5qLGsUXGq%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DlPw1UjCrO1a3tLjVkHtgCiIvtLc%253D)

**3\. 알아서 필요한 파일들을 설치 중이다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FbhN0kh%2FbtsIMSqGtmF%2FAAAAAAAAAAAAAAAAAAAAAC5omGtKKLY7LhjaBkHw20U0lLUwp_W5k42HXkJMnOrU%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DNZWHQRHLNb40hoERBpVCn9Snre4%253D)

**4\. 재부팅해준다.**

```bash
reboot
```

**5\. Setting에서 Keyboard 탭으로 이동해서 \[+\]을 클릭 후 \[Korean\]을 선택하면 재부팅 전에는 없던 "Korean (Hangul)"이 생긴 것을 볼 수 있다. 이것을 클릭 후 추가해준다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fb4xZIc%2FbtsIKCXpt2i%2FAAAAAAAAAAAAAAAAAAAAAIJNmLqSarBUA9w5nmULkBo0v4MvQR58Hf-ureim_b1C%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DEGWdWWyt%252BB7TB2ht7y37TmTb0dM%253D)

재부팅 후 \[Setting\]->\[Keyboard\]->\[+\]->\[Korean\]->\[Korean (Hangul)\]

**6\. 기존에 사용 중이던 "English (US)"는 제거한다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fbpc6ze%2FbtsIMw9iAzm%2FAAAAAAAAAAAAAAAAAAAAAKUbdiXO7-neAcvlqBCz4GX_JHh1Zi8CeuAspxGAvEfE%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DX5r9wSnNV3QvMTLFtlbBEPpzuTg%253D)

**7\. 그리고 Korean (Hangul)의 \[Preferences\]를 선택한다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FFEVgY%2FbtsIKazS5rS%2FAAAAAAAAAAAAAAAAAAAAADWJsukTzXf7bNkTBpkbZn0OG0QgwQaEcNn-LqECJBSB%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3Dd5kThUSDkBNpp6rngk%252FB8%252BU46jY%253D)

**8\. 기존 Toggle Key들을 제거해준다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FdregYN%2FbtsILkV36kF%2FAAAAAAAAAAAAAAAAAAAAAEhkC_gJaDhT_trHSjpTwQg9wFLr8ssMz7d82OJ63vq1%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D5YAamflwUtXYTew2uc0QHR89OU8%253D)

**9\. Toggle Key를 추가해주기 위해 Add를 누른 뒤에 "한영키"(여기서는 Alt\_R로 인식)를 한번만 클릭해준 뒤 \[OK\]를 눌러주면 한영키 설정도 완료되었다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcjCsJR%2FbtsIMGKyUiR%2FAAAAAAAAAAAAAAAAAAAAABLiIbDEfyGztjh2Gjrx4-7YSnqXwfgo3tGw5cRnG2Hw%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3D21l7E9mosO4R75tGwc7y20%252FFQMA%253D)

**10\. 한영키 및 한글 입력이 매우 잘 되는 것을 바로 확인할 수 있다.**

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcLRXxF%2FbtsIM7OGMrP%2FAAAAAAAAAAAAAAAAAAAAACZf5R2hAelZdRBPeRMF0Jb05_ruloTCBDIpnwMTX6Te%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1769871599%26allow_ip%3D%26allow_referer%3D%26signature%3DPu0LEX9KrIGa2QFfj8g%252FwQdETtU%253D)

#### '' 카테고리의 다른 글

| [\[Ubuntu\] 우분투 환경에 Github Desktop 설치하기](https://gosury32.tistory.com/26) (0) | 2024.07.24 |
| --- | --- |
| [\[Ubuntu\] 우분투 환경에 Slack 설치하기](https://gosury32.tistory.com/25) (0) | 2024.07.24 |
| [\[Ubuntu\] sudo apt update && sudo apt upgrade connection failed 오류 해결법](https://gosury32.tistory.com/23) (2) | 2024.07.24 |
| [\[Ubuntu\] 22.04 환경에서 Anaconda 설치하기](https://gosury32.tistory.com/14) (0) | 2024.07.03 |
| [\[Ubuntu\] Terminator 설치 및 테마 설정](https://gosury32.tistory.com/13) (0) | 2024.07.03 |

[NEON MOOD](https://gosury32.tistory.com/) [🏫DGIST. Computer Engineering (Undergraduate)](https://gosury32.tistory.com/)

[상단으로](https://gosury32.tistory.com/#hELLO)