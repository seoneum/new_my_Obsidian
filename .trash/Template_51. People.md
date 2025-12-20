---
<%* let name = tp.file.title; 
let nametag = name.replace(/ /g,"");
let mobile = await tp.system.prompt("핸드폰 번호 입력:");
let email = await tp.system.prompt("이메일 주소:");
-%> 
type: people
tags:
- <% nametag %>
- people
- people/<% nametag %>
aliases: 
group: <% tp.system.suggester(["지인", "저자", "유명인"], ["acquaintance", "author", "influencer"]) %>
organization: 
mobile: <% mobile %>
email: <% email %>
links: 
index: "[[🏷 People]]"
---
# <% tp.file.title %>
## Personal Information
#### Basic Information
- Name: <% name %>
- Year of Birth: 
- Occupation: 
- Field of Expertise: 
#### Contact Information
- Mobile: <% mobile %>
- Office: 
- Email: <% email %>
- Address: 
#### Social Media
- Instagram: 
- Thread: 
- X (Twitter): 
- Linkedin: 
- YouTube: 
- Blog: 
- Other SNS: 
#### Links
- 
## Professional Information
#### Current Position
- Organization: 
- Job Title: 
- Department: 
- Role/Responsibilities: 
#### Field of Work
- Industry: 
- Specialization: 
- Areas of Expertise: 
#### Career History
- Previous Positions:
  - [연도] [직책], [회사/기관]
  - [연도] [직책], [회사/기관]
#### Education
- Highest Degree: 
- Major: 
- Institution: 
- Year of Graduation:
## Professional Background
#### Expertise and Achievements
- %% 학자의 경우: 연구 분야, 주요 저서, 수상 경력 등 %%
- %% 지인/친구의 경우: 특기, 재능, 경력, 프로젝트 경험 등 %%
#### Interests and Knowledge
- %% 전문 분야에 대한 깊이 있는 지식 %%
- %% 취미, 열정, 관심사 %%
## Learning and Inspiration
#### Strengths and Learning Points
- %% 강점, 당신이 배우고 싶은 점 %%
- %% 받은 영감, 조언, 교훈 %%
#### Personal Connection and Memories
- %% 어떻게 만났는지, 함께 한 경험 %%
- %% 개인적 에피소드, 대화 내용 등 %%
## Future Plans and Goals
- %% 단기 및 장기 목표 %%
- %% 협력 가능성, 네트워킹 기회 %%
## Miscellaneous Notes
- %% 그들에 대한 당신의 인상, 생각 %%
- %% 추가로 알아보고 싶은 점 %%
# References
## Personal Publications
- 
## Appendices
- 
## Source
- 


<% await tp.file.move("/70. Collections/71. People/" + tp.file.title) %>
