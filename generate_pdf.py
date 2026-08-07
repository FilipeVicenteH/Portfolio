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
        leftMargin=36,
        rightMargin=36,
        topMargin=24,
        bottomMargin=24
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
        fontSize=9.2,
        leading=11,
        textColor=SECONDARY_COLOR,
        alignment=TA_CENTER,
        spaceAfter=2
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=11.5,
        textColor=PRIMARY_COLOR,
        spaceBefore=4,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.0,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=10.8,
        textColor=PRIMARY_COLOR
    )

    job_company_style = ParagraphStyle(
        'JobCompany',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=10.4,
        textColor=SECONDARY_COLOR
    )

    job_period_style = ParagraphStyle(
        'JobPeriod',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_MUTED,
        alignment=2 # Right
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.4,
        textColor=TEXT_DARK,
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=1
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10.8,
        textColor=PRIMARY_COLOR
    )

    skill_val_style = ParagraphStyle(
        'SkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.8,
        textColor=TEXT_DARK
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("Filipe Vicente Hidalgo", title_style))
    story.append(Spacer(1, 2))
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
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceBefore=1, spaceAfter=3))

    # 2. RESUMO PROFISSIONAL
    story.append(Paragraph("RESUMO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))
    summary_p = (
        "Profissional híbrido com sólida formação acadêmica em <b>Ciência da Computação</b> e <b>Design Gráfico</b>, com experiência "
        "comprovada no desenvolvimento Front-End de aplicações web (React, Next.js 15, TypeScript), engenharia de integrações via APIs/Webhooks, "
        "atendimento técnico de <b>Suporte N1/N2</b> e <b>Customer Success (CS)</b>. Criador da plataforma SaaS <b>UnicoCRM</b> "
        "(gestão de retenção e reconversão de churn) e responsável pelo redesign visual de 30 interfaces da plataforma UnicoDrop. "
        "Habilidade em transformar chamados técnicos e demandas de suporte em soluções definitivas de software e melhorias de UX."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 3))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

    skills_data = [
        [
            Paragraph("<b>Front-End & UI/UX:</b>", skill_label_style),
            Paragraph("HTML5, CSS3, JavaScript (ES6+), React, Next.js 15, TypeScript, Tailwind, Figma, Responsive Design", skill_val_style)
        ],
        [
            Paragraph("<b>Back-End & APIs:</b>", skill_label_style),
            Paragraph("Node.js, APIs RESTful, Webhooks, JSON, Prisma ORM, Neon PostgreSQL Cloud, SQL", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte Técnico N2:</b>", skill_label_style),
            Paragraph("Troubleshooting avançado, análise de logs, payloads de APIs/Webhooks, Helpdesk, redução de SLA, suporte remoto", skill_val_style)
        ],
        [
            Paragraph("<b>Customer Success & Onboarding:</b>", skill_label_style),
            Paragraph("Onboarding técnico de clientes, gestão de churn, retenção de contas, relatórios operacionais (Power BI/Excel)", skill_val_style)
        ],
        [
            Paragraph("<b>Plataformas & Automação:</b>", skill_label_style),
            Paragraph("Shopify, Nuvemshop, instâncias de automação WhatsApp (QR Code / API), disparos SMS e E-mail", skill_val_style)
        ],
        [
            Paragraph("<b>Sistemas & Infraestrutura:</b>", skill_label_style),
            Paragraph("Windows, Linux, macOS, TCP/IP, DNS, Git, GitHub, Montagem & Manutenção de Hardware", skill_val_style)
        ]
    ]

    t_skills = Table(skills_data, colWidths=[150, 390])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.0),
        ('TOPPADDING', (0, 0), (-1, -1), 1.0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 3))

    # 4. HISTÓRICO PROFISSIONAL & PROJETOS
    story.append(Paragraph("HISTÓRICO PROFISSIONAL E PROJETOS EM DESTAQUE", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI, Desenvolvedor & Suporte N2 / CS Specialist", job_title_style)
    j1_company = Paragraph("Unico Drop", job_company_style)
    j1_period = Paragraph("06/2024 &ndash; 08/2026", job_period_style)

    header_table1 = Table([
        [j1_title, j1_period],
        [j1_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 150])
    header_table1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table1)
    story.append(Spacer(1, 1.5))

    j1_bullets = [
        "<b>Projeto UnicoCRM (Full-Stack SaaS):</b> Idealizei e construí do zero uma aplicação web completa (Next.js 15, TypeScript, Tailwind, Prisma, Neon PostgreSQL) para acompanhamento de retenção e reconversão de clientes cancelados. <i>Resultado: centralização do histórico de atendimento, análise dos motivos de churn e recuperação direta de receita (MRR).</i>",
        "<b>Projeto UnicoDrop Redesign Visual (30 Interfaces):</b> Reformulei visualmente 30 telas operacionais (React, Tailwind, Figma) incluindo dashboards de vendas (Facebook/Google Ads), rastreio e DRE financeiro. <i>Resultado: otimização da experiência dos lojistas e diminuição estimada em 40% no tempo de localização de informações.</i>",
        "<b>Projeto Landing Page Diagnóstico Webhook:</b> Desenvolvi landing page de conversão com formulário dinâmico integrado via Webhook para pré-qualificação de clientes. <i>Resultado: automação da captura de leads e agilidade na entrada de novos e-commerces na plataforma.</i>",
        "<b>Atendimento de Suporte N2 & Troubleshooting:</b> Atuação direta em incidentes de maior complexidade, analisando requisições JSON, instâncias de automação de WhatsApp/SMS e integridade de APIs com plataformas como Shopify e Nuvemshop, garantindo baixa taxa de reincidência e SLA reduzido.",
        "<b>Customer Success & Onboarding Técnico:</b> Condução do processo de onboarding de novos lojistas, suporte na configuração de domínios e taxas, treinamentos da ferramenta e elaboração de relatórios estratégicos para apoiar o crescimento e a retenção da carteira de clientes."
    ]
    for bullet in j1_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # Job 2: Levlife
    j2_title = Paragraph("Design & Social Media Specialist | E-commerce", job_title_style)
    j2_company = Paragraph("Levlife", job_company_style)
    j2_period = Paragraph("03/2022 &ndash; 08/2023", job_period_style)

    header_table2 = Table([
        [j2_title, j2_period],
        [j2_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 150])
    header_table2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table2)
    story.append(Spacer(1, 1.5))

    j2_bullets = [
        "Desenvolvimento de landing pages focadas em alta conversão e divulgação de produtos digitais e físicos.",
        "Criação de identidade visual, peças publicitárias e banners promocionais utilizando Photoshop, Illustrator e Figma.",
        "Gestão de catálogos e suporte operacional para e-commerce, garantindo consistência na apresentação dos produtos."
    ]
    for bullet in j2_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # Job 3: 2º Tabelião
    j3_title = Paragraph("Auxiliar de Cartório & Atendimento Técnico", job_title_style)
    j3_company = Paragraph("2º Tabelião de Protestos e Notas de São Caetano do Sul", job_company_style)
    j3_period = Paragraph("05/2021 &ndash; 02/2022", job_period_style)

    header_table3 = Table([
        [j3_title, j3_period],
        [j3_company, Paragraph("", job_period_style)]
    ], colWidths=[390, 150])
    header_table3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table3)
    story.append(Spacer(1, 1.5))

    j3_bullets = [
        "Atendimento direto ao público e suporte a usuários na conferência e processamento de documentos corporativos em alto volume.",
        "Organização de fluxos e dados cadastrais em sistemas internos, garantindo precisão e conformidade com requisitos operacionais."
    ]
    for bullet in j3_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # 5. FORMAÇÃO ACADÊMICA
    story.append(Paragraph("FORMAÇÃO ACADÊMICA", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

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

    t_edu = Table(edu_data, colWidths=[390, 150])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 3))

    # 6. CERTIFICADOS E CURSOS
    story.append(Paragraph("CERTIFICADOS E CURSOS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

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

    t_certs = Table(certs_data, colWidths=[270, 270])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
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
