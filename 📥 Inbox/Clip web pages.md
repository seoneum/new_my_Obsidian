---
title: Clip web pages
source: https://help.obsidian.md/web-clipper/capture
author:
  - "[[Obsidian Help]]"
published: {}
created: 2025-12-16
description: Obsidian Web Clipper 소개 - Obsidian 도움말
tags:
  - "clippings"
migrated_from: CMDS/100. Inbox/140. Web_Clipper/Clip web pages.md
updated: 2026-01-18T16:42:53
domain:
  - cs
cmds: inbox
---
[웹 클리퍼](https://help.obsidian.md/web-clipper) 브라우저 확장 프로그램을 설치하면 브라우저에 따라 여러 가지 방법으로 액세스할 수 있습니다.

1. 브라우저 도구 모음의 Obsidian 아이콘입니다.
2. Hotkeys, 키보드에서 확장을 활성화합니다.
3. 컨텍스트 메뉴, 방문하는 웹 페이지를 마우스 오른쪽 버튼으로 클릭하여.

Obsidian에 페이지를 저장하려면 **Obsidian에 추가** 버튼을 클릭합니다.

## 페이지 캡처

확장을 열면 웹 클리퍼는 [템플릿의](https://help.obsidian.md/web-clipper/templates) 설정에 따라 현재 웹 페이지에서 데이터를 추출합니다. 자체 템플릿을 만들고 [변수 및](https://help.obsidian.md/web-clipper/variables) [필터를](https://help.obsidian.md/web-clipper/filters) 사용하여 출력을 사용자 지정할 수 있습니다.

기본적으로 웹 클리퍼는 페이지의 다른 요소를 제외하고 주요 기사 콘텐츠만을 지능적으로 추출하려고 시도합니다. 그러나 다음과 같은 방법으로 이러한 동작을 재정의할 수 있습니다.

- 사용자 지정 템플릿이 있는 경우 템플릿을 사용합니다.
- 선택이 있으면 선택을 사용합니다. 당신은 사용할 수 있습니다 `Ctrl/Cmd+A` 전체 페이지를 선택합니다.
- [하이라이트가](https://help.obsidian.md/web-clipper/highlight) 있으면 하이라이트를 사용합니다.

## 이미지 다운로드

이미지는 웹 클리퍼를 사용할 때 자동으로 다운로드되지 않습니다. 대신 이미지는 웹 기반 URL에 연결됩니다. 이렇게하면 볼트의 공간을 절약 할 수 있지만 이미지는 오프라인으로 액세스 할 수 없거나 URL이 작동을 중지하는 경우 표시됩니다.

**현재 파일에 대한 첨부 파일 다운로드라는** [명령을](https://help.obsidian.md/plugins/command-palette) 사용하여 Obsidian의 모든 파일에 대한 이미지를 다운로드 할 수 있습니다**.** 이 명령은 Obsidian의 핫키에도 매핑될 수 있습니다.

## 핫키

웹 클리퍼에는 워크플로 속도를 높이는 데 사용할 수 있는 키보드 단축키가 포함되어 있습니다. 키 매핑을 변경하려면 **웹 클리퍼 설정** → **일반으로** 이동하여 브라우저의 지침을 따르십시오. 핫키 편집을 지원하지 않는 Safari를 제외한 모든 브라우저에서 매핑을 변경할 수 있습니다.

| Action | macOS | Windows/Linux |
| --- | --- | --- |
| Open clipper | `Cmd+Shift+O` | `Ctrl+Shift+O` |
| Quick clip | `Opt+Shift+O` | `Alt+Shift+O` |
| Toggle highlighter mode | `Opt+Shift+H` | `Alt+Shift+H` |

## Interface functionality

The Web Clipper interface is divided into four sections:

- **Template** dropdown to switch between your saved [templates](https://help.obsidian.md/web-clipper/templates) added in Web Clipper settings.
- **More (...)** button to display page variables you can use in templates.
- **Highlighter** button to turn on [highlighting](https://help.obsidian.md/web-clipper/highlight).
- **Cog** button to open Web Clipper settings.

- **Add to Obsidian** button to save data to Obsidian.
- **Vault** dropdown to switch between saved vaults added in Web Clipper settings.
- **Folder** field to define which folder to save to.
- **Interpreter** to run [natural language prompts](https://help.obsidian.md/web-clipper/interpreter) on the page.