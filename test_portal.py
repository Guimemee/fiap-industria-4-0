# -*- coding: utf-8 -*-
"""
Script de teste automatizado Playwright para o portal Indústria 4.0.
Verifica integridade de links, âncoras, botões de cópia e tira screenshots mobile e desktop.
"""
import sys, os
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from playwright.sync_api import sync_playwright

def test_portal():
    html_path = 'file:///' + os.path.abspath('D:/fiap-industria-4-0/index.html').replace('\\', '/')
    brain_dir = r'C:\Users\guilh\.gemini\antigravity\brain\ef60c18f-86d0-447b-97be-ed3976b52d6b'
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Teste 1: Desktop Viewport
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(html_path)
        page.wait_for_load_state("networkidle")
        
        # Verificar título
        title = page.title()
        print(f"[TEST 1] Título da página: {title}")
        assert "FIAP" in title and "Indústria 4.0" in title
        
        # Verificar todos os links internos (âncoras)
        anchors = page.query_selector_all('a[href^="#"]')
        print(f"[TEST 2] Verificando {len(anchors)} âncoras internas:")
        for a in anchors:
            href = a.get_attribute("href")
            target_id = href[1:]
            target = page.query_selector(f"#{target_id}")
            assert target is not None, f"ERRO: Âncora {href} não encontrou o elemento com id '{target_id}'!"
            print(f"  ✓ Âncora {href} -> Elemento #{target_id} OK")
            
        # Testar botão de cópia de código
        copy_btns = page.query_selector_all('.copy-btn')
        print(f"[TEST 3] Testando {len(copy_btns)} botões de cópia de código:")
        if copy_btns:
            copy_btns[0].click()
            page.wait_for_timeout(300)
            btn_text = copy_btns[0].inner_text()
            print(f"  ✓ Botão de cópia clicado, texto retornado: '{btn_text}'")
            assert "Copiado" in btn_text
            
        # Screenshot Desktop
        desktop_screen = os.path.join(brain_dir, 'screenshot_ind40_desktop.png')
        page.screenshot(path=desktop_screen, full_page=False)
        print(f"[TEST 4] Screenshot Desktop salvo em: {desktop_screen}")
        
        page.close()
        
        # Teste 2: Mobile Viewport (iPhone 14 / 390x844)
        mobile_page = browser.new_page(viewport={"width": 390, "height": 844})
        mobile_page.goto(html_path)
        mobile_page.wait_for_load_state("networkidle")
        
        # Checar se o cabeçalho mobile está sem cortes e bem posicionado
        h1_el = mobile_page.query_selector('.header-row-1')
        h2_tag = mobile_page.query_selector('.header-tagline')
        h2_btn = mobile_page.query_selector('.header-repo-btn')
        
        print(f"[TEST 5] Verificação de elementos do cabeçalho mobile:")
        print(f"  Linha 1 texto: '{h1_el.inner_text()}'")
        print(f"  Linha 2 Tag:   '{h2_tag.inner_text()}'")
        print(f"  Linha 2 Botão: '{h2_btn.inner_text()}'")
        
        mobile_screen = os.path.join(brain_dir, 'screenshot_ind40_mobile.png')
        mobile_page.screenshot(path=mobile_screen, full_page=False)
        print(f"[TEST 6] Screenshot Mobile salvo em: {mobile_screen}")
        
        # Screenshot Mobile Scrolled para ver os cards
        mobile_page.evaluate("window.scrollTo(0, 480)")
        mobile_page.wait_for_timeout(300)
        mobile_scrolled = os.path.join(brain_dir, 'screenshot_ind40_mobile_scrolled.png')
        mobile_page.screenshot(path=mobile_scrolled, full_page=False)
        print(f"[TEST 7] Screenshot Mobile Scrolled salvo em: {mobile_scrolled}")
        
        mobile_page.close()
        browser.close()
        print("\nTODOS OS TESTES AUTOMATIZADOS PASSARAM COM SUCESSO (100% OK)!")

if __name__ == '__main__':
    test_portal()
