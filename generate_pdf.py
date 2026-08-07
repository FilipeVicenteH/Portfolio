import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_resume(output_filename):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=18,
        bottomMargin=18
    )

    styles = getSampleStyleSheet()

    # Color Palette
    PRIMARY_COLOR = colors.HexColor('#0F172A')   # Slate Dark Navy
    SECONDARY_COLOR = colors.HexColor('#0D9488') # Teal Accent
    TEXT_DARK = colors.HexColor('#334155')       # Slate dark text
    TEXT_MUTED = colors.HexColor('#64748B')      # Slate muted
    LINE_COLOR = colors.HexColor('#CBD5E1')      # Border line

    # Styles
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=20,
        textColor=PRIMARY_COLOR,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=10.5,
        textColor=SECONDARY_COLOR,
        alignment=TA_CENTER,
        spaceAfter=1
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=9.8,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=11.0,
        textColor=PRIMARY_COLOR,
        spaceBefore=3,
        spaceAfter=1
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.9,
        leading=10.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=PRIMARY_COLOR
    )

    job_company_style = ParagraphStyle(
        'JobCompany',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.0,
        textColor=SECONDARY_COLOR
    )

    job_period_style = ParagraphStyle(
        'JobPeriod',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.0,
        textColor=TEXT_MUTED,
        alignment=2 # Right
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.7,
        leading=9.9,
        textColor=TEXT_DARK,
        leftIndent=9,
        firstLineIndent=-5,
        spaceAfter=1.5
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.2,
        textColor=PRIMARY_COLOR
    )

    skill_val_style = ParagraphStyle(
        'SkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_DARK
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("Filipe Vicente Hidalgo", title_style))
    story.append(Spacer(1, 1))
    story.append(Paragraph("Desenvolvedor Front-End &nbsp;|&nbsp; Suporte Técnico N2 &nbsp;|&nbsp; Customer Success Specialist", subtitle_style))
    story.append(Spacer(1, 1))

    contact_text = (
        "São Paulo, SP &bull; filipe_vicente@hotmail.com &bull; (11) 96615-2956<br/>"
        "LinkedIn: <a href='https://www.linkedin.com/in/filipevicentehidalgo' color='#0D9488'>linkedin.com/in/filipevicentehidalgo</a> &bull; "
        "GitHub: <a href='https://github.com/FilipeVicenteH' color='#0D9488'>github.com/FilipeVicenteH</a><br/>"
        "Behance: <a href='https://www.behance.net/filipevicenteh' color='#0D9488'>behance.net/filipevicenteh</a> &bull; "
        "Portfólio: <a href='https://filipevicenteh.vercel.app' color='#0D9488'>filipevicenteh.vercel.app</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 1))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceBefore=1, spaceAfter=2))

    # 2. RESUMO PROFISSIONAL (100% HUMANIZADO)
    story.append(Paragraph("RESUMO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))
    summary_p = (
        "<b>Desenvolvedor Front-End e Analista de Suporte Técnico N2</b> com formação em <b>Ciência da Computação</b> e <b>Design Gráfico</b>. "
        "Atuação focada no desenvolvimento de interfaces SaaS (React, Next.js 15, TypeScript), integrações via APIs/Webhooks e resolução de chamados "
        "N2 de alta complexidade com análise de logs (Postman/cURL). Criador da aplicação <b>UnicoCRM</b> para gestão de retenção e reconversão de clientes "
        "cancelados, e responsável pelo <b>Redesign Visual de 30 interfaces</b> da plataforma UnicoDrop. Experiência prática em Customer Success, "
        "onboarding de lojistas e sustentação de sistemas."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 2))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    skills_data = [
        [
            Paragraph("<b>Front-End & UI/UX:</b>", skill_label_style),
            Paragraph("HTML5, CSS3, JavaScript (ES6+), React, Next.js 15 (App Router), TypeScript, Tailwind CSS, Bootstrap, Figma, Design System", skill_val_style)
        ],
        [
            Paragraph("<b>Back-End & APIs:</b>", skill_label_style),
            Paragraph("Node.js, APIs RESTful, Webhooks, JSON Payloads, Prisma ORM, Neon PostgreSQL Cloud, SQL", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte Técnico N2:</b>", skill_label_style),
            Paragraph("Troubleshooting avançado, depuração de logs HTTP (Postman, Insomnia, cURL), Status Codes (4xx/5xx), gestão de chamados (SLA), suporte remoto", skill_val_style)
        ],
        [
            Paragraph("<b>Customer Success & CS:</b>", skill_label_style),
            Paragraph("Onboarding técnico de lojistas, análise de churn/MRR, estratégias de retenção, suporte a parâmetros de gateway/frete, dashboards em Power BI e Excel", skill_val_style)
        ],
        [
            Paragraph("<b>Plataformas & Automação:</b>", skill_label_style),
            Paragraph("Shopify, Nuvemshop, instâncias de automação WhatsApp (QR Code / API), disparos de SMS e E-mail", skill_val_style)
        ],
        [
            Paragraph("<b>Sistemas & Ferramentas:</b>", skill_label_style),
            Paragraph("Windows, Linux, macOS, TCP/IP, DNS, Git, GitHub, Vercel Deploy, Montagem & Manutenção de Hardware", skill_val_style)
        ]
    ]

    t_skills = Table(skills_data, colWidths=[140, 408])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.6),
        ('TOPPADDING', (0, 0), (-1, -1), 0.6),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 2))

    # 4. PROJETOS DE SOFTWARE & SISTEMAS SAAS
    story.append(Paragraph("PROJETOS DE SOFTWARE & SISTEMAS SAAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    projects_list = [
        "<b>UnicoCRM &ndash; Gestão de Retenção & Reconversão de Churn (<a href='https://unico-crm.vercel.app/relatorios' color='#0D9488'>unico-crm.vercel.app/relatorios</a>):</b> "
        "Desenvolvi do zero uma aplicação SaaS Full-Stack em <b>Next.js 15 (App Router e Server Actions), TypeScript, Tailwind CSS, Prisma ORM e Neon PostgreSQL Cloud</b>. "
        "O sistema oferece relatórios dinâmicos de cancelamento, categorização por motivo (preço, suporte, bugs, concorrência), histórico unificado de interações e pipeline de reativação de clientes. "
        "<i>Resultado: automação da régua de retenção e mitigação direta de perda de receita recorrente (MRR).</i>",

        "<b>UnicoDrop Redesign Visual & UI/UX (30 Interfaces Codadas) (<a href='https://telas-unico.vercel.app' color='#0D9488'>telas-unico.vercel.app</a>):</b> "
        "Liderei a reformulação estética e funcional da plataforma, construindo o Design System no <b>Figma</b> e recodificando <b>30 telas operacionais em React, Tailwind CSS e ApexCharts</b> "
        "organizadas em 4 módulos (E-commerce/Pedidos, Dashboards Ads/Financeiro DRE, Automação Mensageria e Configurações). "
        "<i>Resultado: eliminação de poluição visual e redução estimada em 40% no tempo de localização de informações operacionais pelos lojistas.</i>",

        "<b>UnicoDrop Diagnóstico &ndash; Landing Page & Captação via Webhook (<a href='https://teste-web-hook.vercel.app' color='#0D9488'>teste-web-hook.vercel.app</a>):</b> "
        "Projetei e codifiquei landing page responsiva de alta conversão com fluxo interativo em 7 perguntas dinâmicas de auditoria, construída com <b>HTML5, CSS3, JavaScript ES6+ assíncrono e Webhooks HTTP</b>. "
        "Dispara payloads de leads qualificados em tempo real para o CRM/Vendas. <i>Resultado: eliminação de triagem manual e aceleração da entrada de novos e-commerces.</i>"
    ]
    for proj_item in projects_list:
        story.append(Paragraph(f"&bull; {proj_item}", bullet_style))
    story.append(Spacer(1, 2))

    # 5. HISTÓRICO PROFISSIONAL
    story.append(Paragraph("HISTÓRICO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI, Desenvolvedor & Suporte N2 / CS Specialist", job_title_style)
    j1_company = Paragraph("Unico Drop", job_company_style)
    j1_period = Paragraph("06/2024 &ndash; 08/2026", job_period_style)

    header_table1 = Table([
        [j1_title, j1_period],
        [j1_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 158])
    header_table1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table1)
    story.append(Spacer(1, 1))

    j1_bullets = [
        "<b>Suporte Técnico N2 & Troubleshooting de Integrações:</b> Diagnostiquei e resolvi chamados técnicos de alta complexidade (N2), realizando a depuração detalhada de payloads JSON, logs de requisições HTTP via <b>Postman, Insomnia e cURL</b> e verificação de Status Codes (4xx/5xx). Atuação direta na análise de instâncias de mensageria (WhatsApp QR Code / SMS) e sincronização de pedidos e estoques com e-commerces (<b>Shopify e Nuvemshop</b>), garantindo baixa taxa de reincidência e SLA reduzido.",
        "<b>Customer Success (CS) & Onboarding Técnico de Lojistas:</b> Responsável pelo onboarding técnico de novos clientes da plataforma, auxiliando na parametrização de domínios customizados, Pixels de conversão, tabelas de frete e taxas de gateway. Acompanhamento ativo da retenção de contas, prevenção de churn e elaboração de dashboards operacionais estratégicos em Power BI para suporte às tomadas de decisão."
    ]
    for bullet in j1_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 2))

    # Job 2: Levlife
    j2_title = Paragraph("Design & Social Media Specialist | E-commerce", job_title_style)
    j2_company = Paragraph("Levlife", job_company_style)
    j2_period = Paragraph("03/2022 &ndash; 08/2023", job_period_style)

    header_table2 = Table([
        [j2_title, j2_period],
        [j2_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 158])
    header_table2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table2)
    story.append(Spacer(1, 1))

    j2_bullets = [
        "Desenvolvimento de landing pages focadas em alta conversão e promoção visual de produtos e campanhas digitais.",
        "Criação de identidade visual, peças publicitárias, materiais gráficos e banners utilizando Photoshop, Illustrator e Figma."
    ]
    for bullet in j2_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 2))

    # Job 3: 2º Tabelião
    j3_title = Paragraph("Auxiliar de Cartório & Atendimento Técnico", job_title_style)
    j3_company = Paragraph("2º Tabelião de Protestos e Notas de São Caetano do Sul", job_company_style)
    j3_period = Paragraph("05/2021 &ndash; 02/2022", job_period_style)

    header_table3 = Table([
        [j3_title, j3_period],
        [j3_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 158])
    header_table3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table3)
    story.append(Spacer(1, 1))

    j3_bullets = [
        "Atendimento direto ao público e conferência minuciosa de documentos corporativos e jurídicos em alto volume."
    ]
    for bullet in j3_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 2))

    # 6. FORMAÇÃO ACADÊMICA
    story.append(Paragraph("FORMAÇÃO ACADÊMICA", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    edu_data = [
        [
            Paragraph("<b>Bacharelado em Ciência da Computação</b> &ndash; <font color='#64748B'>Centro Univ. Descomplica (UniAmérica)</font>", skill_val_style),
            Paragraph("<font color='#64748B'>Concluído: 07/2026</font>", job_period_style)
        ],
        [
            Paragraph("<b>Tecnólogo em Design Gráfico</b> &ndash; <font color='#64748B'>Faculdade Uninove</font>", skill_val_style),
            Paragraph("<font color='#64748B'>Concluído: 07/2020</font>", job_period_style)
        ]
    ]

    t_edu = Table(edu_data, colWidths=[390, 158])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.6),
        ('TOPPADDING', (0,0), (-1,-1), 0.6),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 2))

    # 7. CERTIFICADOS E CURSOS
    story.append(Paragraph("CERTIFICADOS E CURSOS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    certs_data = [
        [
            Paragraph("&bull; <b>Web Design</b> &ndash; Jorge Street (2014)", skill_val_style),
            Paragraph("&bull; <b>Modelagem 3D</b> &ndash; All Net (2014)", skill_val_style)
        ],
        [
            Paragraph("&bull; <b>Inglês Intermediário</b> &ndash; Count Down (2016)", skill_val_style),
            Paragraph("&bull; <b>Excel Intermediário</b> &ndash; Uninove (2019)", skill_val_style)
        ]
    ]

    t_certs = Table(certs_data, colWidths=[270, 278])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.6),
        ('TOPPADDING', (0,0), (-1,-1), 0.6),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    doc.build(story)

if __name__ == "__main__":
    out_dir = r"C:\Users\User\Desktop\Portfolio"
    out_file = os.path.join(out_dir, "Curriculo_Filipe_Vicente_Hidalgo.pdf")
    create_resume(out_file)
    print(f"PDF generated at: {out_file}")
