# -*- coding: utf-8 -*-
# event-builder-common-settings.html(원본)을 베이스로
# 화면설계서 프레임(우측 기능 설명 패널 + 좌우 연동 + 캔버스 스케일)을 입혀
# specs/event_common_setting.html 을 생성한다.
import io, sys

SRC = r"C:\Users\min17\OneDrive - NEXON COMPANY\바탕 화면\이벤트 플랫폼\화면 제작 샘플\event-builder-common-settings.html"
DST = r"C:\Users\min17\OneDrive - NEXON COMPANY\바탕 화면\기획\harness\specs\event_common_setting.html"

html = io.open(SRC, encoding="utf-8").read()

def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, "anchor not unique (%d): %s" % (n, old[:80])
    html = html.replace(old, new)

# ── 1. 타이틀 ──
rep("<title>Event Builder — 이벤트 화면 + 세부 화면 설정</title>",
    "<title>이벤트 공통 설정 - 이벤트 빌더 화면설계서</title>")

# ── 2. 기능 섹션에 data-id + onclick 부여 ──
rep('<div class="Setup_Preview_Canvas" data-name="Setup_Preview_Canvas" data-node-id="9427:71708">',
    '<div class="Setup_Preview_Canvas" data-id="01" onclick="specActivate(\'01\')" data-name="Setup_Preview_Canvas" data-node-id="9427:71708">')
rep('data-name="Common_PeriodSetting_Section_EventPeriod" data-node-id="9260:9720">',
    'data-id="02" onclick="specActivate(\'02\')" data-name="Common_PeriodSetting_Section_EventPeriod" data-node-id="9260:9720">')
rep('data-name="Common_PeriodSetting_Section_RewardPeriod" data-node-id="9260:9793">',
    'data-id="03" onclick="specActivate(\'03\')" data-name="Common_PeriodSetting_Section_RewardPeriod" data-node-id="9260:9793">')
rep('data-name="Common_PeriodSetting_Section_MissionReset" data-node-id="9260:9862">',
    'data-id="04" onclick="specActivate(\'04\')" data-name="Common_PeriodSetting_Section_MissionReset" data-node-id="9260:9862">')
rep('data-name="Common_PeriodSetting_BgColor" data-node-id="9260:9891">',
    'data-id="05" onclick="specActivate(\'05\')" data-name="Common_PeriodSetting_BgColor" data-node-id="9260:9891">')
rep('<div class="Nav_LNB_Setting" data-name="Nav_LNB_Setting" data-node-id="7661:6901">',
    '<div class="Nav_LNB_Setting" data-id="06" onclick="specActivate(\'06\')" data-name="Nav_LNB_Setting" data-node-id="7661:6901">')
rep('<div class="Common_BgSetting" data-name="Common_BgSetting" data-node-id="7661:6927">',
    '<div class="Common_BgSetting" data-id="08" onclick="specActivate(\'08\')" data-name="Common_BgSetting" data-node-id="7661:6927">')
rep('<div class="Common_RewardPopup_Setting" data-name="Common_RewardPopup_Setting" data-node-id="7661:7797">',
    '<div class="Common_RewardPopup_Setting" data-id="10" onclick="specActivate(\'10\')" data-name="Common_RewardPopup_Setting" data-node-id="7661:7797">')
rep('<div class="Common_FuncBtn_Setting" data-name="Common_FuncBtn_Setting" data-node-id="9466:91285">',
    '<div class="Common_FuncBtn_Setting" data-id="12" onclick="specActivate(\'12\')" data-name="Common_FuncBtn_Setting" data-node-id="9466:91285">')

# ── 3. 스펙 프레임용 CSS 오버라이드 (</style> 직전 삽입) ──
CHROME_CSS = """
/* ════════════════════════════════════════════
   SPEC CHROME — 화면설계서 프레임 (원본 위 오버라이드)
════════════════════════════════════════════ */
:root {
  --bg: #ffffff; --bg2: #f5f5f3; --bg3: #eeece8;
  --text: #1a1a18; --text2: #6b6a65; --text3: #9c9a92;
  --border: rgba(0,0,0,0.12); --border2: rgba(0,0,0,0.2);
  --info-bg: #e6f1fb; --info-text: #0c447c; --info-border: rgba(24,95,165,0.3);
  --warn-bg: #faeeda; --warn-text: #633806; --warn-border: rgba(186,117,23,0.3);
  --radius: 8px; --radius-lg: 12px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1e1e1c; --bg2: #2a2a27; --bg3: #333330;
    --text: #e8e6de; --text2: #9c9a92; --text3: #6b6a65;
    --border: rgba(255,255,255,0.1); --border2: rgba(255,255,255,0.2);
    --info-bg: #0c2d4a; --info-text: #85b7eb; --info-border: rgba(55,138,221,0.3);
    --warn-bg: #2d1f00; --warn-text: #fac775; --warn-border: rgba(186,117,23,0.3);
  }
}
html, body { height: auto; overflow: auto; background: var(--bg); }
body { max-width: 2000px; margin: 0 auto; font-size: 13px; color: var(--text); }

.breadcrumb { padding: 12px 16px; font-size: 11px; color: var(--text2);
              border-bottom: 0.5px solid var(--border);
              font-family: -apple-system, 'Pretendard', sans-serif; }
.breadcrumb a { color: var(--info-text); text-decoration: none; }

.layout { display: grid; grid-template-columns: 1fr 320px; gap: 16px;
          padding: 16px; min-height: calc(100vh - 40px); align-items: start; }

.screen-panel { background: var(--bg2); border-radius: var(--radius-lg);
                padding: 16px; border: 0.5px solid var(--border); min-width: 0; }
.screen-panel-title { font-size: 11px; color: var(--text2); margin-bottom: 12px;
                      font-family: -apple-system, 'Pretendard', sans-serif; }

/* 원본 빌더 레이아웃을 인플로우로 전환 */
.event-builder-root { display: flex; gap: 14px; align-items: flex-start;
                      height: auto; overflow: visible; }
.preview-wrapper { flex: 1; min-width: 0; overflow: hidden;
                   background: #555; border-radius: 8px; }
.Setup_Preview_Canvas { transform-origin: top left; }
.Setup_ScreenDetail_Panel { height: auto; border-radius: 8px;
                            position: sticky; top: 16px;
                            max-height: calc(100vh - 32px); overflow-y: auto; }

/* 관리자 팝업: 원본 그대로 화면 전체 fixed 오버레이로 표시.
   작은 화면에서 잘리지 않도록 최대 크기만 보정 */
.lnb-popup-overlay, .bg-popup-overlay, .reward-popup-overlay,
.funcbtn-popup-overlay, .add-popup-overlay { padding: 24px; }
.Common_FuncBtn_DetailPopup { max-width: calc(100vw - 48px);
                              max-height: calc(100vh - 48px); overflow-y: auto;
                              min-height: 0; }
.funcbtn-popup-left { min-width: 0; width: 50%; }
.Nav_LNB_Setting_Popup, .Common_BgSetting_Popup,
.Common_RewardPopup_DetailPopup, .Common_FuncBtn_AddPopup {
  max-width: calc(100vw - 48px); max-height: calc(100vh - 48px); overflow-y: auto; }

/* 기능 섹션 활성/강조 */
[data-id].spec-active    { outline: 2px solid #1c6bff;  outline-offset: 2px; border-radius: 4px; }
[data-id].spec-highlight { outline: 2px dashed rgba(28,107,255,0.55); outline-offset: 2px; border-radius: 4px; }
[data-id] { cursor: pointer; }

/* ── 우측 설명 패널 ── */
.desc-panel { background: var(--bg); border-radius: var(--radius-lg);
              border: 0.5px solid var(--border); padding: 16px;
              overflow-y: auto; max-height: calc(100vh - 56px);
              position: sticky; top: 16px;
              font-family: -apple-system, 'Pretendard', sans-serif; }
.desc-panel-title { font-size: 11px; font-weight: 500; color: var(--text2); margin-bottom: 6px; }
.desc-purpose { font-size: 11px; color: var(--text2); line-height: 1.6;
                background: var(--bg2); border-radius: var(--radius);
                padding: 10px; margin-bottom: 12px; }
.desc-group-label { font-size: 10px; font-weight: 600; color: var(--text3);
                    letter-spacing: 0.05em; margin: 12px 0 6px; }
.desc-list-item { display: flex; align-items: center; gap: 8px;
                  padding: 7px 10px; border-radius: var(--radius);
                  cursor: pointer; transition: background 0.12s;
                  border: 0.5px solid transparent; margin-bottom: 3px; }
.desc-list-item:hover { background: var(--bg2); border-color: var(--border); }
.desc-list-item.active { background: var(--info-bg); border-color: var(--info-border); }
.desc-list-num { font-size: 10px; font-weight: 500; color: var(--info-text);
                 min-width: 30px; font-family: monospace; }
.desc-list-name { font-size: 12px; color: var(--text); flex: 1; }
.desc-list-arrow { font-size: 10px; color: var(--text3); transition: transform 0.15s; }
.desc-list-item.active .desc-list-arrow { transform: rotate(90deg); }
.desc-detail { display: none; margin: 0 0 6px 0; padding: 12px 14px;
               background: var(--bg2); border-radius: var(--radius);
               border: 0.5px solid var(--border); }
.desc-detail.active { display: block; }
.desc-id { font-size: 11px; font-weight: 500; color: var(--info-text); margin-bottom: 4px; }
.desc-name { font-size: 13px; font-weight: 500; margin-bottom: 8px; color: var(--text); }
.desc-body { font-size: 12px; color: var(--text2); line-height: 1.7; }
.desc-body ul { padding-left: 16px; margin: 0; }
.desc-body li { margin: 0 0 5px; }
.desc-body li:last-child { margin-bottom: 0; }
.tag { display: inline-block; font-size: 10px; padding: 1px 8px;
       border-radius: 100px; margin: 0 3px 6px 0; }
.tag-type { background: var(--bg2); color: var(--text2); border: 0.5px solid var(--border); }
.tag-ui { background: var(--warn-bg); color: var(--warn-text); }
.info-block { margin-top: 10px; padding: 10px; border-radius: var(--radius);
              font-size: 11px; background: var(--info-bg); color: var(--info-text); line-height: 1.7; }
.warn-block { margin-top: 10px; padding: 10px; border-radius: var(--radius);
              font-size: 11px; background: var(--warn-bg); color: var(--warn-text); line-height: 1.7; }
.block-title { font-weight: 500; display: block; margin-bottom: 4px; }
.hint { font-size: 11px; color: var(--text3); text-align: center; padding: 12px 0 2px;
        font-family: -apple-system, 'Pretendard', sans-serif; }

/* ── 파라미터 레이어명 칩 (노션 '[공통] 전체 템플릿 공통 파라미터' 기준) ── */
.spec-layer-chip {
  display: inline-block; font-family: Consolas, monospace;
  font-size: 10px; line-height: 16px; color: #1c6bff;
  background: #eef4ff; border: 1px solid #d5e3ff; border-radius: 4px;
  padding: 0 6px; margin-left: 6px; vertical-align: middle; white-space: nowrap;
}
.desc-body code {
  font-family: Consolas, monospace; font-size: 11px;
  color: var(--info-text); background: var(--info-bg);
  padding: 0 4px; border-radius: 3px; white-space: nowrap;
}

/* ── 재화 획득/사용 내역 (정의서 §5-4 — HTML 선반영) ── */
.Common_Popup_CurrencyLog {
  position: absolute; inset: 0;
  width: 1780px; height: 890px;
  display: none; z-index: 200;
}
.Common_Popup_CurrencyLog.visible { display: block; }
.Common_Popup_CurrencyLog_Overlay {
  position: absolute; inset: 0;
  background: rgba(0,0,0,0.7);
}
.Common_Popup_CurrencyLog .Common_Popup_Modal {
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  width: 1300px; height: 760px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.2);
  display: flex; flex-direction: column;
  overflow: hidden;
}
"""
rep("</style>", CHROME_CSS + "\n</style>")

# ── 4. <body> 직후: 브레드크럼 + 레이아웃 + 좌측 패널 오픈 ──
CHROME_OPEN = """<body>

<div class="breadcrumb">
  <a href="../index.html">이벤트 빌더</a> &gt; 이벤트 화면 설정 &gt; 이벤트 공통 설정 (공통기능 / 선택공통기능)
</div>

<div class="layout">
  <!-- ════════ 좌측: 화면 목업 (원본 빌더 화면 재현) ════════ -->
  <div class="screen-panel">
    <div class="screen-panel-title">Event Builder &gt; 이벤트 화면 설정 &gt; 세부 화면 설정 — 모든 이벤트 템플릿 공통 · 설정 변경 시 미리보기 즉시 반영</div>
"""
rep("<body>\n", CHROME_OPEN)

# ── 5. </body> 직전: 힌트 + 좌측 패널 닫기 + 우측 설명 패널 + 스펙 JS ──
DESC_PANEL = """
    <!-- ── 재화 획득/사용 내역 팝업 설정 (HTML 선반영, md [확인 필요]) ── -->
    <div class="funcbtn-popup-overlay" id="currencyPopupOverlay">
      <div class="Common_FuncBtn_AddPopup" style="gap:20px;">
        <div class="add-popup-header">
          <p class="add-popup-title">재화 획득/사용 내역 팝업 설정</p>
          <button class="add-popup-close" id="currencyPopupXBtn" aria-label="닫기">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M5 5L15 15M15 5L5 15" stroke="#222" stroke-width="1.6" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
        <div class="add-popup-divider"></div>

        <!-- ① 재화 내역 버튼 -->
        <div class="funcbtn-section">
          <p class="funcbtn-section-title">재화 내역 버튼 <span class="spec-layer-chip">@:currency_history_btn:{locale}</span></p>
          <div class="funcbtn-radio-group">
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-btn-type" value="default" checked>
              <span class="funcbtn-radio-label">기본 버튼 사용</span>
            </label>
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-btn-type" value="custom">
              <span class="funcbtn-radio-label">이미지 등록</span>
            </label>
          </div>
          <div class="popup-upload-row" id="currencyBtnUploadArea" style="display:none;">
            <div class="popup-upload-wrap">
              <div class="popup-upload-box" data-spec-target="cur-btn-kr">
                <div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div>
                <span class="popup-upload-hint">이미지를 등록해주세요</span>
              </div>
              <p class="popup-upload-lang">KR</p>
            </div>
            <div class="popup-upload-wrap">
              <div class="popup-upload-box" data-spec-target="cur-btn-en">
                <div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div>
                <span class="popup-upload-hint">이미지를 등록해주세요</span>
              </div>
              <p class="popup-upload-lang">EN</p>
            </div>
          </div>
        </div>

        <!-- ② 팝업 내 확인 버튼 -->
        <div class="funcbtn-section">
          <p class="funcbtn-section-title">팝업 내 확인 버튼 <span class="spec-layer-chip">@:currency_history_confirm_btn:{locale}</span></p>
          <div class="funcbtn-radio-group">
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-confirm-type" value="default" checked>
              <span class="funcbtn-radio-label">기본 버튼 사용</span>
            </label>
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-confirm-type" value="custom">
              <span class="funcbtn-radio-label">이미지 등록</span>
            </label>
          </div>
          <div class="popup-upload-row" id="currencyConfirmUploadArea" style="display:none;">
            <div class="popup-upload-wrap">
              <div class="popup-upload-box" data-spec-target="cur-confirm-kr">
                <div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div>
                <span class="popup-upload-hint">이미지를 등록해주세요</span>
              </div>
              <p class="popup-upload-lang">KR</p>
            </div>
            <div class="popup-upload-wrap">
              <div class="popup-upload-box" data-spec-target="cur-confirm-en">
                <div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div>
                <span class="popup-upload-hint">이미지를 등록해주세요</span>
              </div>
              <p class="popup-upload-lang">EN</p>
            </div>
          </div>
        </div>

        <!-- ③ 재화 내역 테이블 설정 -->
        <div class="funcbtn-section">
          <p class="funcbtn-section-title">재화 내역 테이블 설정 <span class="spec-layer-chip">@:currency_history_table_bg</span></p>
          <div class="funcbtn-radio-group">
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-table-bg" value="default" checked>
              <span class="funcbtn-radio-label">기본 테이블 사용</span>
            </label>
            <label class="funcbtn-radio-option">
              <input class="funcbtn-radio" type="radio" name="cur-table-bg" value="custom">
              <span class="funcbtn-radio-label">배경 이미지 등록(1300×760px)</span>
            </label>
          </div>
          <div id="currencyTableBgUpload" style="display:none;">
            <div class="popup-upload-row">
              <div class="popup-upload-wrap">
                <div class="popup-upload-box" data-spec-target="cur-table-bg">
                  <div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div>
                  <span class="popup-upload-hint">이미지를 등록해주세요</span>
                </div>
                <p class="popup-upload-lang">테이블 배경</p>
              </div>
            </div>
          </div>
        </div>

        <div class="add-popup-footer" style="justify-content:space-between;">
          <button class="funcbtn-delete-btn" id="currencyDeleteBtn">버튼 삭제</button>
          <button class="funcbtn-save-btn" id="currencyPopupSaveBtn">저장</button>
        </div>
      </div>
    </div>

    <div class="hint">좌측 설정 영역을 클릭하면 해당 기능 설명이 열려요 · "세부 설정"을 누르면 설정 팝업이 아래에 표시돼요 · 미리보기의 [보상 받기]/[유의 사항]/[리워드 수령 내역] 버튼도 직접 눌러볼 수 있어요</div>
  </div><!-- /screen-panel -->

  <!-- ════════ 우측: 기능 설명 패널 ════════ -->
  <div class="desc-panel">
    <div class="desc-panel-title">기능 설명 · EVENT_COMMON_SETTING</div>
    <div class="desc-purpose">모든 이벤트 템플릿(주사위, 출석, 미션, 가챠 등)에 공통 적용되는 설정.<br><br>
      · 레이어명: <b>@:&lt;slug&gt;:&lt;locale&gt;</b> — prefix @, slug 소문자 35자 이하, locale은 다국어(localeAware) 항목만<br>
      · 타입: image / text 2종 (색상값·ID도 text)<br>
      · 매칭 기준: 피그마 레이어명<br>
      · 컴포넌트 네이밍: [Scope]_[Component]_[Element] (정의서 v4.0)</div>

    <div class="desc-group-label">■ 공통기능 — 모든 템플릿 기본 포함</div>

    <div class="desc-list-item" id="list-01" onclick="specToggle('01')" onmouseenter="specHighlight('01')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_01</span><span class="desc-list-name">세부 화면 설정 패널</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-01">
      <div class="desc-id">EVENT_COMMON_SETTING_01</div>
      <div class="desc-name">세부 화면 설정 패널 (공통)</div>
      <span class="tag tag-type">조회</span><span class="tag tag-ui">우측 고정 패널 + 아코디언 5종</span>
      <div class="desc-body"><ul>
        <li>라디오·컬러피커 설정은 미리보기에 <b>즉시 반영</b></li>
        <li>팝업 내 설정은 <b>저장 시에만 반영</b> — 취소·X·오버레이 닫기 시 변경사항 폐기</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-02" onclick="specToggle('02')" onmouseenter="specHighlight('02')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_02</span><span class="desc-list-name">기간 UI — 이벤트 기간</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-02">
      <div class="desc-id">EVENT_COMMON_SETTING_02</div>
      <div class="desc-name">기간 UI 설정 — 이벤트 기간 (공통)</div>
      <span class="tag tag-type">수정</span><span class="tag tag-ui">라디오 8개 · 즉시 반영</span>
      <div class="desc-body"><ul>
        <li>실제 기간 값은 <b>이벤트 등록 정보에서 조회</b> — 콘솔에서는 표기 형식만 선택</li>
        <li>기본값: YYYY.MM.DD 포맷</li>
        <li>"시스템 기간 표기 없음" 선택 시 이벤트 기간 행 미노출</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>타이머 표기의 실시간 갱신 주기.</div>
    </div>

    <div class="desc-list-item" id="list-03" onclick="specToggle('03')" onmouseenter="specHighlight('03')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_03</span><span class="desc-list-name">기간 UI — 리워드 수령 기간</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-03">
      <div class="desc-id">EVENT_COMMON_SETTING_03</div>
      <div class="desc-name">기간 UI 설정 — 리워드 수령 기간 (공통)</div>
      <span class="tag tag-type">수정</span><span class="tag tag-ui">라디오 8개 · 즉시 반영</span>
      <div class="desc-body"><ul>
        <li>기본값: 시스템 기간 표기 없음</li>
        <li>이벤트·리워드 기간 <b>모두 "표기 없음"이면 기간 영역 전체 미노출</b></li>
        <li>한쪽만 표기 시 1줄(Single), 양쪽 표기 시 2줄(Double)</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-04" onclick="specToggle('04')" onmouseenter="specHighlight('04')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_04</span><span class="desc-list-name">기간 UI — 미션 초기화 기간</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-04">
      <div class="desc-id">EVENT_COMMON_SETTING_04</div>
      <div class="desc-name">기간 UI 설정 — 미션 초기화 기간 (공통)</div>
      <span class="tag tag-type">수정</span><span class="tag tag-ui">라디오 2개 · 즉시 반영</span>
      <div class="desc-body"><ul>
        <li>적용 시 초기화 카운트다운 노출, 미적용 시 컴포넌트 미노출</li>
        <li>기본값: 타이머 적용</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>정의서상 Mission_ResetInfo는 미션형 전용 Scope. 모든 템플릿 공통인지, 미션형 템플릿 한정 조건부 노출인지 확인 필요.</div>
    </div>

    <div class="desc-list-item" id="list-05" onclick="specToggle('05')" onmouseenter="specHighlight('05')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_05</span><span class="desc-list-name">기간 UI — 배경 색상</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-05">
      <div class="desc-id">EVENT_COMMON_SETTING_05</div>
      <div class="desc-name">기간 UI 설정 — 배경 색상 (공통)</div>
      <span class="tag tag-type">수정</span><span class="tag tag-ui">컬러피커 + HEX · 즉시 반영</span>
      <div class="desc-body"><ul>
        <li>파라미터: <code>@:date_color</code> — text · 언어 공용 · <b>필수</b> · #RRGGBB</li>
        <li>배경 색상만 등록 — <b>그라데이션은 시스템 자동 처리</b></li>
        <li>기간 정보·초기화 타이머 배경에 공통 적용</li>
        <li>텍스트 색상 #FFFFFF 고정 · 미지정 시 #000000 fallback</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-06" onclick="specToggle('06')" onmouseenter="specHighlight('06')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_06</span><span class="desc-list-name">LNB 설정(배너)</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-06">
      <div class="desc-id">EVENT_COMMON_SETTING_06</div>
      <div class="desc-name">LNB 설정(배너) (공통)</div>
      <span class="tag tag-type">조회</span><span class="tag tag-ui">아코디언 + 세부 설정 버튼</span>
      <div class="desc-body"><ul>
        <li>현재 설정 중인 이벤트의 LNB Active 항목(배너)을 커스터마이징 — 등록 항목은 _07 팝업 참조</li>
        <li>기본 텍스트는 최대 3줄 노출</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-07" onclick="specOpenPopup('lnbDetailOpenBtn','07')" onmouseenter="specHighlight('06')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_07</span><span class="desc-list-name">LNB 설정 팝업</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-07">
      <div class="desc-id">EVENT_COMMON_SETTING_07</div>
      <div class="desc-name">LNB 설정 팝업</div>
      <span class="tag tag-type">수정/저장</span><span class="tag tag-ui">모달 (라디오+업로드+TextInput)</span>
      <div class="desc-body"><ul>
        <li>옵션 A 통이미지: <code>@:lnb:{locale}</code> — image · 언어별 · <b>280×160px</b> · 적용 시 텍스트 숨김</li>
        <li>옵션 B 이미지+텍스트: 배경 <code>@:lnb_bg</code>(언어 공용) + 이벤트명 <code>@:lnb_txt:{locale}</code>(언어별 · <b>최대 24자</b>)</li>
        <li>텍스트 미입력 시 텍스트 숨김 · 이미지 삭제 후 저장 시 기본 상태 복구</li>
        <li>저장 시에만 반영 — 취소·닫기 시 폐기</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>샘플 미리보기는 KR 기준으로만 반영(EN은 등록만 가능) — 실서비스는 localeAware 파라미터로 언어별 노출.</div>
    </div>

    <div class="desc-list-item" id="list-08" onclick="specToggle('08')" onmouseenter="specHighlight('08')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_08</span><span class="desc-list-name">배경 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-08">
      <div class="desc-id">EVENT_COMMON_SETTING_08</div>
      <div class="desc-name">배경 설정 (공통)</div>
      <span class="tag tag-type">조회</span><span class="tag tag-ui">아코디언 + 세부 설정 버튼</span>
      <div class="desc-body"><ul>
        <li>배경 이미지 등록은 _09 팝업에서 진행</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-09" onclick="specOpenPopup('bgDetailOpenBtn','09')" onmouseenter="specHighlight('08')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_09</span><span class="desc-list-name">배경 이미지 설정 팝업</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-09">
      <div class="desc-id">EVENT_COMMON_SETTING_09</div>
      <div class="desc-name">배경 이미지 설정 팝업</div>
      <span class="tag tag-type">수정/저장</span><span class="tag tag-ui">모달 (업로드 KR/EN)</span>
      <div class="desc-body"><ul>
        <li>파라미터: <code>@:event_bg:{locale}</code> — image · 언어별 통이미지 · <b>필수</b></li>
        <li>LNB 제외 전체 배경(1500×890) · Z-index 최하단 · 이벤트별 교체</li>
        <li>이미지 URL 동적 수신 · 권장 사이즈 별도 명시</li>
        <li>저장 시에만 반영 · 삭제 후 저장 시 배경 초기화</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-10" onclick="specToggle('10')" onmouseenter="specHighlight('10')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_10</span><span class="desc-list-name">보상 획득 결과 팝업 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-10">
      <div class="desc-id">EVENT_COMMON_SETTING_10</div>
      <div class="desc-name">보상 획득 결과 팝업 설정 (공통)</div>
      <span class="tag tag-type">수정</span><span class="tag tag-ui">라디오 3종 + 컬러피커 2종 · 즉시 반영</span>
      <div class="desc-body"><ul>
        <li>표기법은 <b>피그마 등록 변수 패턴으로 시스템 자동 추론</b> — A: 리워드명+수량 / B: 리워드명(기본) / C: 수량만</li>
        <li><code>@:reward_popup_txt_color</code> — A/B에서 사용 · 기본 #FFFFFF</li>
        <li><code>@:reward_popup_count_color</code> — A/C에서 사용 · 기본 #000000 · 수량 텍스트는 흰색 고정</li>
        <li>보상 팝업은 공통 모달(1300×760) 사용 · 수량 표기 형식 X99,999</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-11" onclick="specOpenPopup('rewardDetailOpenBtn','11')" onmouseenter="specHighlight('10')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_11</span><span class="desc-list-name">보상 팝업 세부 설정 팝업</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-11">
      <div class="desc-id">EVENT_COMMON_SETTING_11</div>
      <div class="desc-name">보상 획득 결과 팝업 세부 설정 팝업</div>
      <span class="tag tag-type">수정/저장</span><span class="tag tag-ui">모달 (라디오 2조 + 업로드)</span>
      <div class="desc-body"><ul>
        <li>팝업 배경 <code>@:reward_popup_bg</code> — 언어 공용 · 선택 · <b>미등록 시 프로젝트별 공통 기본 팝업</b></li>
        <li>확인 버튼 <code>@:reward_popup_btn:{locale}</code> — 언어별 · 선택 · 미등록 시 공통 기본 버튼</li>
        <li>저장 시에만 반영 · 기본 선택 시 기본 스타일 복구</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>샘플 미리보기는 KR 기준으로만 반영 — 실서비스는 localeAware 파라미터로 언어별 노출.</div>
    </div>

    <div class="desc-group-label">■ 선택공통기능 — 선택적 추가</div>

    <div class="desc-list-item" id="list-12" onclick="specToggle('12')" onmouseenter="specHighlight('12')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_12</span><span class="desc-list-name">기능 버튼 추가 및 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-12">
      <div class="desc-id">EVENT_COMMON_SETTING_12</div>
      <div class="desc-name">기능 버튼 추가 및 설정 (선택공통)</div>
      <span class="tag tag-type">조회/수정</span><span class="tag tag-ui">아코디언 + 리스트(드래그) + 버튼</span>
      <div class="desc-body"><ul>
        <li>추가된 버튼은 화면 우측 상단 Header_Actions에 노출 (240×70)</li>
        <li>초기 기본 구성: 유의사항 · 리워드 수령 내역</li>
        <li>세부 설정: 유의사항 → _14 / 수령 내역 → _15 / 재화 내역 → _16</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>드래그 순서 변경이 Header_Actions 노출 순서에 반영되는지 확인 필요.</div>
    </div>

    <div class="desc-list-item" id="list-13" onclick="specOpenPopup('funcBtnAddBtn','13')" onmouseenter="specHighlight('12')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_13</span><span class="desc-list-name">기능 버튼 추가 팝업</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-13">
      <div class="desc-id">EVENT_COMMON_SETTING_13</div>
      <div class="desc-name">기능 버튼 추가 팝업</div>
      <span class="tag tag-type">수정/저장</span><span class="tag tag-ui">모달 (체크박스 3종)</span>
      <div class="desc-body"><ul>
        <li>오픈 시 현재 활성 상태가 체크박스에 반영 · "추가" 시 일괄 적용(해제 항목은 숨김)</li>
        <li>재화 획득/사용 내역은 <b>미니게임/상점교환 이벤트에서만 노출</b></li>
        <li>취소·닫기 시 변경 미적용</li>
      </ul></div>
      <div class="info-block"><span class="block-title">정의서 반영</span>재화 획득/사용 내역은 md v1.1에 미니게임/상점교환 이벤트 한정 노출 항목으로 정의됨 (세부 설정 → _16).</div>
    </div>

    <div class="desc-list-item" id="list-14" onclick="specOpenPopup('noticeDetailOpenBtn','14')" onmouseenter="specHighlight('12')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_14</span><span class="desc-list-name">유의사항 팝업 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-14">
      <div class="desc-id">EVENT_COMMON_SETTING_14</div>
      <div class="desc-name">유의사항 팝업 설정 팝업</div>
      <span class="tag tag-type">수정/저장</span><span class="tag tag-ui">모달 (라디오 3조 + 업로드 + Textarea)</span>
      <div class="desc-body"><ul>
        <li>진입 버튼 <code>@:notice_btn:{locale}</code> — 선택 · 미등록 시 서버 기본(텍스트형 버튼)</li>
        <li>배경 옵션 A 통이미지: <code>@:notice_img:{locale}</code> — <b>1300×760px</b>, 텍스트 포함 이미지</li>
        <li>배경 옵션 B 텍스트: <b>레이어명 없음 — 콘솔에서만 입력</b> · 최대 2,000자 · 초과 시 스크롤 · 기본 이미지는 시스템 제공(프로젝트별 사전 등록)</li>
        <li>옵션 A/B는 상호 배타</li>
        <li>확인 버튼 <code>@:notice_confirm_btn:{locale}</code> — 선택 · 미등록 시 서버 기본</li>
      </ul></div>
    </div>

    <div class="desc-list-item" id="list-15" onclick="specOpenPopup('claimHistoryDetailOpenBtn','15')" onmouseenter="specHighlight('12')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_15</span><span class="desc-list-name">리워드 수령 내역 팝업 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-15">
      <div class="desc-id">EVENT_COMMON_SETTING_15</div>
      <div class="desc-name">리워드 수령 내역 팝업 설정 팝업</div>
      <span class="tag tag-type">수정/저장/삭제</span><span class="tag tag-ui">모달 (라디오 3조 + 업로드 + 버튼 삭제)</span>
      <div class="desc-body"><ul>
        <li>진입 버튼 <code>@:reward_history_btn:{locale}</code> — 언어별 · 선택 · 미등록 시 서버 기본</li>
        <li>확인 버튼 <code>@:reward_history_confirm_btn:{locale}</code> — 언어별 · 선택</li>
        <li>테이블 배경 <code>@:reward_history_table_bg</code> — 언어 공용 · 선택 · 미등록 시 기본 테이블 UI</li>
        <li>테이블 컬럼(구분/리워드/지급 개수/지급일)은 <b>서버 기본 데이터 — 파라미터 없음</b></li>
        <li><b>버튼 삭제</b>: Header_Actions 제거 + 설정 초기화 + 추가 팝업 체크 동기화</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>테이블 배경 권장 사이즈(샘플 00×00) · 버튼 삭제 시 Confirm 없이 즉시 삭제(샘플 기준) — 운영 정책 확인 필요.</div>
    </div>

    <div class="desc-list-item" id="list-16" onclick="specOpenPopup('currencyDetailOpenBtn','16')" onmouseenter="specHighlight('12')" onmouseleave="specUnhighlight()">
      <span class="desc-list-num">_16</span><span class="desc-list-name">재화 획득/사용 내역 팝업 설정</span><span class="desc-list-arrow">›</span>
    </div>
    <div class="desc-detail" id="desc-16">
      <div class="desc-id">EVENT_COMMON_SETTING_16</div>
      <div class="desc-name">재화 획득/사용 내역 팝업 설정 팝업 (미니게임/상점교환 한정)</div>
      <span class="tag tag-type">수정/저장/삭제</span><span class="tag tag-ui">모달 (라디오 3조 + 업로드 + 버튼 삭제)</span>
      <div class="desc-body"><ul>
        <li><b>미니게임/상점교환 이벤트에서만 노출</b></li>
        <li>진입 버튼 <code>@:currency_history_btn:{locale}</code> — 언어별 · 선택 · 미등록 시 서버 기본</li>
        <li>확인 버튼 <code>@:currency_history_confirm_btn:{locale}</code> — 언어별 · 선택</li>
        <li>테이블 배경 <code>@:currency_history_table_bg</code> — 언어 공용 · 선택 · <b>1300×760px</b> · 미등록 시 기본 테이블 UI</li>
        <li>테이블 컬럼(일시/구분/획득·사용/보유 재화)은 <b>서버 기본 데이터 — 파라미터 없음</b></li>
        <li><b>버튼 삭제</b>: Header_Actions 제거 + 추가 팝업 체크 동기화</li>
      </ul></div>
      <div class="warn-block"><span class="block-title">⚠ 확인 필요</span>버튼 표기명("재화 내역" 임시 사용 중) 확정 필요 · 파라미터 변수명(트리 구조 path)은 엔지니어 확정 대기.</div>
    </div>

    <div class="warn-block" style="margin-top:14px;">
      <span class="block-title">Validation 요약</span>
      · LNB 텍스트 최대 24자 (KR/EN)<br>
      · 유의사항 텍스트 최대 2,000자 (KR/EN)<br>
      · 이미지 파일만 업로드 가능 (image/*)<br>
      · 필수 입력 없음 — 모든 설정 기본값 존재<br>
      · 팝업 변경사항은 저장 시에만 반영, 취소 시 폐기<br>
      · 확장자/용량 제한, 권장 사이즈 강제 여부 [확인 필요]
    </div>
  </div><!-- /desc-panel -->
</div><!-- /layout -->

<script>
/* ════════ SPEC FRAME — 좌우 연동 + 캔버스 스케일 ════════ */
var SPEC_PARENT = { '07':'06', '09':'08', '11':'10', '13':'12', '14':'12', '15':'12', '16':'12' };
var specSuppress = false; /* 아코디언 자동 펼침 중 desc 활성화 억제 */
function specParent(id) { return SPEC_PARENT[id] || id; }

function specActivate(id) {
  if (specSuppress) return;
  document.querySelectorAll('[data-id]').forEach(function(s){ s.classList.remove('spec-active'); });
  var sec = document.querySelector('[data-id="'+specParent(id)+'"]');
  if (sec) sec.classList.add('spec-active');
  document.querySelectorAll('.desc-list-item').forEach(function(i){ i.classList.remove('active'); });
  document.querySelectorAll('.desc-detail').forEach(function(d){ d.classList.remove('active'); });
  var li = document.getElementById('list-'+id);
  if (li) { li.classList.add('active'); li.scrollIntoView({block:'nearest'}); }
  var de = document.getElementById('desc-'+id);
  if (de) de.classList.add('active');
}
function specToggle(id) {
  var de = document.getElementById('desc-'+id);
  if (de && de.classList.contains('active')) {
    de.classList.remove('active');
    var li = document.getElementById('list-'+id);
    if (li) li.classList.remove('active');
    document.querySelectorAll('[data-id]').forEach(function(s){ s.classList.remove('spec-active'); });
  } else {
    specActivate(id);
    var sec = document.querySelector('[data-id="'+specParent(id)+'"]');
    if (sec) sec.scrollIntoView({behavior:'smooth', block:'nearest'});
  }
}
function specHighlight(id) {
  specUnhighlight();
  var sec = document.querySelector('[data-id="'+specParent(id)+'"]');
  if (sec) sec.classList.add('spec-highlight');
}
function specUnhighlight() {
  document.querySelectorAll('[data-id]').forEach(function(s){ s.classList.remove('spec-highlight'); });
}
function specOpenPopup(btnId, descId) {
  var b = document.getElementById(btnId);
  if (b) b.click(); /* 원본 핸들러가 팝업 오픈 + 아래 리스너가 desc 동기화 */
  else specActivate(descId);
}

/* 캔버스 스케일 — 1780×890 원본을 컨테이너 폭에 맞춰 축소 */
function fitCanvas() {
  var wrap = document.querySelector('.preview-wrapper');
  var canvas = document.querySelector('.Setup_Preview_Canvas');
  if (!wrap || !canvas) return;
  var s = Math.min(1, wrap.clientWidth / 1780);
  canvas.style.transform = 'scale(' + s + ')';
  wrap.style.height = Math.round(890 * s) + 'px';
}
window.addEventListener('resize', fitCanvas);

document.addEventListener('DOMContentLoaded', function () {
  /* 아코디언 기본 펼침 (원본 초기값: 모두 접힘) — desc 활성화는 억제 */
  specSuppress = true;
  ['periodSettingToggle','lnbSettingToggle','bgSettingToggle','rewardPopupSettingToggle','funcBtnSettingToggle']
    .forEach(function(id){
      var t = document.getElementById(id);
      if (t && !t.classList.contains('is-open')) t.click();
    });
  specSuppress = false;

  /* 세부 설정 버튼 → 설명 패널 동기화 (팝업은 원본 핸들러가 화면 오버레이로 표시) */
  [['lnbDetailOpenBtn','07'],
   ['bgDetailOpenBtn','09'],
   ['rewardDetailOpenBtn','11'],
   ['funcBtnAddBtn','13'],
   ['noticeDetailOpenBtn','14'],
   ['claimHistoryDetailOpenBtn','15'],
   ['currencyDetailOpenBtn','16']
  ].forEach(function(cfg){
    var b = document.getElementById(cfg[0]);
    if (!b) return;
    b.addEventListener('click', function(e){
      e.stopPropagation(); /* 부모 섹션 specActivate가 덮어쓰지 않도록 */
      specActivate(cfg[1]);
    });
  });

  /* ════════ 재화 획득/사용 내역 — HTML 선반영 (md [확인 필요]) ════════ */
  var currencyActive = false;
  var specPending = {};
  var currencyBtn = document.querySelector('[data-name="Common_Btn_Text [재화내역]"]');
  var currencyItem = document.getElementById('funcBtnItem_CurrencyLog');
  var currencyOverlay = document.getElementById('currencyPopupOverlay');
  var currencyCanvasPopup = document.getElementById('Common_Popup_CurrencyLog');

  /* 추가 팝업 오픈 시 체크 상태 동기화 (원본 리스너 이후 실행) */
  document.getElementById('funcBtnAddBtn').addEventListener('click', function () {
    document.getElementById('addChk_CurrencyLog').checked = currencyActive;
  });
  /* 추가 확정 → 리스트/Header_Actions 반영 */
  document.getElementById('addPopupConfirmBtn').addEventListener('click', function () {
    currencyActive = document.getElementById('addChk_CurrencyLog').checked;
    if (currencyBtn)  currencyBtn.style.display  = currencyActive ? '' : 'none';
    if (currencyItem) currencyItem.style.display = currencyActive ? '' : 'none';
  });

  /* 미리보기 [재화 내역] 버튼 → 캔버스 팝업 */
  if (currencyBtn) currencyBtn.addEventListener('click', function () {
    currencyCanvasPopup.classList.add('visible');
  });
  function closeCurrencyCanvasPopup() { currencyCanvasPopup.classList.remove('visible'); }
  document.getElementById('currencyPopupCloseBtn').addEventListener('click', closeCurrencyCanvasPopup);
  document.getElementById('currencyFooterBtn').addEventListener('click', closeCurrencyCanvasPopup);
  document.querySelector('.Common_Popup_CurrencyLog_Overlay').addEventListener('click', closeCurrencyCanvasPopup);

  /* 세부 설정 팝업 오픈/닫기 */
  document.getElementById('currencyDetailOpenBtn').addEventListener('click', function () {
    currencyOverlay.classList.add('visible');
    currencyOverlay.querySelectorAll('.popup-upload-box:not([data-spec-init])').forEach(specInitUpload);
  });
  function closeCurrencyDetail() { currencyOverlay.classList.remove('visible'); }
  document.getElementById('currencyPopupXBtn').addEventListener('click', closeCurrencyDetail);
  currencyOverlay.addEventListener('click', function (e) { if (e.target === currencyOverlay) closeCurrencyDetail(); });

  /* 라디오 → 업로드 영역 토글 */
  document.querySelectorAll('input[name="cur-btn-type"]').forEach(function (r) {
    r.addEventListener('change', function () {
      document.getElementById('currencyBtnUploadArea').style.display = this.value === 'custom' ? 'flex' : 'none';
    });
  });
  document.querySelectorAll('input[name="cur-confirm-type"]').forEach(function (r) {
    r.addEventListener('change', function () {
      document.getElementById('currencyConfirmUploadArea').style.display = this.value === 'custom' ? 'flex' : 'none';
    });
  });
  document.querySelectorAll('input[name="cur-table-bg"]').forEach(function (r) {
    r.addEventListener('change', function () {
      document.getElementById('currencyTableBgUpload').style.display = this.value === 'custom' ? 'block' : 'none';
    });
  });

  /* 저장 → 버튼/확인 버튼/테이블 배경 반영 */
  function specApplyBtnImage(btn, img, mode) {
    if (!btn) return;
    if (mode === 'default' || img === 'reset') {
      btn.style.backgroundImage = ''; btn.style.backgroundColor = '';
      btn.style.backgroundSize = ''; btn.style.backgroundPosition = '';
      btn.style.color = '';
    } else if (mode === 'custom' && img) {
      btn.style.backgroundColor = 'transparent';
      btn.style.backgroundImage = 'url(' + img + ')';
      btn.style.backgroundSize = 'cover';
      btn.style.backgroundPosition = 'center';
      btn.style.color = 'transparent';
    }
  }
  document.getElementById('currencyPopupSaveBtn').addEventListener('click', function () {
    specApplyBtnImage(currencyBtn, specPending['cur-btn-kr'],
      document.querySelector('input[name="cur-btn-type"]:checked').value);
    specApplyBtnImage(document.getElementById('currencyFooterBtn'), specPending['cur-confirm-kr'],
      document.querySelector('input[name="cur-confirm-type"]:checked').value);
    var modal = document.getElementById('currencyModal');
    var tb = document.querySelector('input[name="cur-table-bg"]:checked').value;
    var bg = specPending['cur-table-bg'];
    if (tb === 'default' || bg === 'reset') {
      modal.style.backgroundImage = ''; modal.classList.remove('has-bg-image');
    } else if (tb === 'custom' && bg) {
      modal.style.backgroundImage = 'url(' + bg + ')';
      modal.style.backgroundSize = 'cover';
      modal.style.backgroundPosition = 'center';
      modal.classList.add('has-bg-image');
    }
    closeCurrencyDetail();
  });

  /* 버튼 삭제 → Header_Actions 제거 + 체크 상태 동기화 (샘플 기준 Confirm 없음 — [확인 필요]) */
  document.getElementById('currencyDeleteBtn').addEventListener('click', function () {
    if (currencyBtn)  currencyBtn.style.display  = 'none';
    if (currencyItem) currencyItem.style.display = 'none';
    currencyActive = false;
    closeCurrencyDetail();
  });

  /* 업로드 박스 (스펙 전용 — 원본 initUploadBox는 클로저 내부라 별도 구현) */
  function specInitUpload(box) {
    if (box.hasAttribute('data-spec-init')) return;
    box.setAttribute('data-spec-init', '1');
    var input = document.createElement('input');
    input.type = 'file'; input.accept = 'image/*'; input.style.display = 'none';
    document.body.appendChild(input);
    box.addEventListener('click', function (e) {
      if (e.target.closest('.upload-remove-btn')) return;
      input.value = ''; input.click();
    });
    input.addEventListener('change', function () {
      var f = input.files[0]; if (!f) return;
      var rd = new FileReader();
      rd.onload = function (ev) {
        var url = ev.target.result, t = box.dataset.specTarget;
        specPending[t] = url;
        box.classList.add('has-image');
        box.style.padding = '0';
        box.style.backgroundImage = 'url(' + url + ')';
        box.innerHTML = '<button class="upload-remove-btn" type="button" title="이미지 삭제">✕</button>';
        box.querySelector('.upload-remove-btn').addEventListener('click', function (ev2) {
          ev2.stopPropagation();
          specPending[t] = 'reset';
          box.classList.remove('has-image');
          box.style.padding = ''; box.style.backgroundImage = '';
          box.innerHTML = '<div class="popup-upload-plus"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="#9397a1" stroke-width="1.5" stroke-linecap="round"/></svg></div><span class="popup-upload-hint">이미지를 등록해주세요</span>';
          box.removeAttribute('data-spec-init');
          specInitUpload(box);
        });
      };
      rd.readAsDataURL(f);
    });
  }

  /* ── 레이어명 칩 주입 — 노션 '이벤트 템플릿 파라메터 정의 › [공통] 전체 템플릿 공통 파라미터' 기준 ── */
  function specChip(el, name) {
    if (!el) return;
    var s = document.createElement('span');
    s.className = 'spec-layer-chip';
    s.textContent = name;
    el.appendChild(s);
  }
  /* 기간 UI — 배경 색상 (그라데이션은 시스템 자동 처리) */
  specChip(document.querySelector('.Common_PeriodSetting_BgColor_Picker'), '@:date_color');
  /* 보상 획득 결과 팝업 — 색상 */
  specChip(document.querySelector('#rewardTextColorRow .reward-color-label'), '@:reward_popup_txt_color');
  specChip(document.querySelector('#rewardBgColorRow .reward-color-label'), '@:reward_popup_count_color');
  /* LNB 설정 팝업 — 옵션 A 통이미지 / 옵션 B 배경+텍스트 */
  specChip(document.querySelector('#lnbPopupOverlay .popup-image-section-title'), '@:lnb:{locale}');
  specChip(document.querySelector('#lnbPopupOverlay .popup-text-section-title'), '@:lnb_bg');
  document.querySelectorAll('#lnbPopupOverlay .popup-text-maxlen').forEach(function (el) {
    specChip(el, '@:lnb_txt:{locale}');
  });
  /* 배경 이미지 설정 팝업 */
  specChip(document.querySelector('#bgPopupOverlay .bg-popup-section-title'), '@:event_bg:{locale}');
  /* 보상 획득 결과 팝업 세부 설정 */
  var rdTitles = document.querySelectorAll('#rewardPopupOverlay .reward-detail-section-title');
  specChip(rdTitles[0], '@:reward_popup_bg');
  specChip(rdTitles[1], '@:reward_popup_btn:{locale}');
  /* 유의사항 팝업 설정 — 순서: 버튼 / 배경 입력 방식 / 확인 버튼 */
  var ntTitles = document.querySelectorAll('#noticePopupOverlay .funcbtn-section-title');
  specChip(ntTitles[0], '@:notice_btn:{locale}');
  specChip(ntTitles[1], '@:notice_img:{locale}');
  specChip(ntTitles[2], '@:notice_confirm_btn:{locale}');
  /* 리워드 수령 내역 팝업 설정 — 순서: 버튼 / 확인 버튼 / 테이블 */
  var chTitles = document.querySelectorAll('#claimHistoryPopupOverlay .funcbtn-section-title');
  specChip(chTitles[0], '@:reward_history_btn:{locale}');
  specChip(chTitles[1], '@:reward_history_confirm_btn:{locale}');
  specChip(chTitles[2], '@:reward_history_table_bg');

  fitCanvas();
  setTimeout(fitCanvas, 100);
});
</script>
</body>"""
rep("</body>", DESC_PANEL)

# ── 6. 재화 획득/사용 내역 — HTML 선반영 (md [확인 필요]) ──
# 6-1. 기능 버튼 추가 팝업: 체크박스 활성화
rep('<input class="add-popup-checkbox" type="checkbox" id="addChk_CurrencyLog" data-btn="currencyLog" disabled>',
    '<input class="add-popup-checkbox" type="checkbox" id="addChk_CurrencyLog" data-btn="currencyLog">')

# 6-2. Header_Actions: [재화내역] 버튼 추가 (초기 미노출 — 기능 버튼 추가로 활성화)
rep('data-name="Common_Btn_Text [수령내역]" data-node-id="9427:71715">리워드 수령 내역</button>',
    'data-name="Common_Btn_Text [수령내역]" data-node-id="9427:71715">리워드 수령 내역</button>\n'
    '          <button class="Common_Btn_Text" style="display:none;"\n'
    '                  data-name="Common_Btn_Text [재화내역]">재화 내역</button>')

# 6-3. 기능 버튼 아이템 리스트: 재화 항목 추가 (초기 숨김)
rep("""              세부 설정
            </button>
          </div>

        </div>
      </div>
    </div><!-- /Common_FuncBtn_Setting -->""",
    """              세부 설정
            </button>
          </div>

          <!-- 재화 획득/사용 내역 (HTML 선반영) -->
          <div class="funcbtn-item" data-name="Common_FuncBtn_Setting_Item" id="funcBtnItem_CurrencyLog" style="display:none;">
            <div class="funcbtn-item-left">
              <div class="funcbtn-menu-icon" title="드래그로 순서 변경">
                <span></span><span></span><span></span>
              </div>
              <span class="funcbtn-item-label">재화 획득/사용 내역</span>
            </div>
            <button class="funcbtn-detail-btn" id="currencyDetailOpenBtn"
                    data-name="Common_FuncBtn_Setting_Item_DetailBtn">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M7 2v10M2 7h10" stroke="#5f646f" stroke-width="1.4" stroke-linecap="round"/>
              </svg>
              세부 설정
            </button>
          </div>

        </div>
      </div>
    </div><!-- /Common_FuncBtn_Setting -->""")

# 6-4. 캔버스: Common_Popup_CurrencyLog 팝업 (정의서 §5-4 구조, History 팝업 패턴 재사용)
CURRENCY_POPUP = """
      <!-- ── Common_Popup_CurrencyLog (정의서 §5-4 — HTML 선반영, 컬럼명 [확인 필요]) ── -->
      <div class="Common_Popup_CurrencyLog" id="Common_Popup_CurrencyLog"
           data-name="Common_Popup_CurrencyLog">

        <div class="Common_Popup_CurrencyLog_Overlay"
             data-name="Common_Popup_CurrencyLog_Overlay"></div>

        <!-- Modal (1300×760) -->
        <div class="Common_Popup_Modal" id="currencyModal" data-name="Common_Popup_Modal">

          <div class="Common_Popup_Modal_Header" data-name="Common_Popup_Modal_Header">
            <div class="Common_Popup_Modal_BackBtn"></div>
            <p class="Common_Popup_Modal_Header_Title">재화 획득/사용 내역</p>
            <button class="Common_Popup_Modal_CloseBtn" id="currencyPopupCloseBtn" aria-label="닫기">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
                <path d="M6 6L22 22M22 6L6 22" stroke="#000" stroke-width="2.4" stroke-linecap="round"/>
              </svg>
            </button>
          </div>

          <!-- Table (History 테이블 스타일 재사용 — 컬럼명은 서버 기본 데이터: 일시/구분/획득·사용/보유 재화) -->
          <div class="Common_Popup_History_Table" data-name="Common_Popup_CurrencyLog_Table">
            <div class="Common_Popup_History_Table_Header">
              <div class="Common_Popup_History_Table_Cell"><p>일시</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>구분</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>획득·사용</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>보유 재화</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>획득</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>+000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>사용</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>-000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>획득</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>+000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>사용</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>-000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>획득</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>+000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
            <div class="Common_Popup_History_Table_Row">
              <div class="Common_Popup_History_Table_Cell"><p>0000.00.00 / PM 00:00</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>사용</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>-000,000</p></div>
              <div class="Common_Popup_History_Table_Cell"><p>000,000</p></div>
            </div>
          </div>

          <div class="Common_Popup_Modal_Footer" data-name="Common_Popup_Modal_Footer">
            <button class="Common_Popup_Modal_Footer_Btn" id="currencyFooterBtn">확인</button>
          </div>

        </div><!-- /Common_Popup_Modal -->
      </div><!-- /Common_Popup_CurrencyLog -->
"""
rep("</div><!-- /Common_Popup_History -->",
    "</div><!-- /Common_Popup_History -->\n" + CURRENCY_POPUP)

io.open(DST, "w", encoding="utf-8").write(html)
print("OK lines:", html.count("\n"))
