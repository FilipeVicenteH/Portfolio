import os
import fitz # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_resume(output_filename):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=28,
        rightMargin=28,
        topMargin=14,
        bottomMargin=14
    )

    styles = getSampleStyleSheet()

    # Palette
    PRIMARY_COLOR = colors.HexColor('#0F172A')   # Slate Dark Navy
    SECONDARY_COLOR = colors.HexColor('#0D9488') # Teal Accent
    TEXT_DARK = colors.HexColor('#334155')       # Slate dark text
    TEXT_MUTED = colors.HexColor('#64748B')      # Slate muted
    LINE_COLOR = colors.HexColor('#CBD5E1')      # Border line

    # Typography & Styles optimized for 1-page fit
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16.5,
        leading=18.5,
        textColor=PRIMARY_COLOR,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.0,
        textColor=SECONDARY_COLOR,
        alignment=TA_CENTER,
        spaceAfter=1
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.2,
        textColor=PRIMARY_COLOR,
        spaceBefore=2.0,
        spaceAfter=0.5
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=9.8,
        textColor=PRIMARY_COLOR
    )

    job_company_style = ParagraphStyle(
        'JobCompany',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.5,
        textColor=SECONDARY_COLOR
    )

    job_period_style = ParagraphStyle(
        'JobPeriod',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=TEXT_MUTED,
        alignment=2 # Right
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.4,
        textColor=TEXT_DARK,
        leftIndent=8,
        firstLineIndent=-4,
        spaceAfter=1.0
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.3,
        leading=9.4,
        textColor=PRIMARY_COLOR
    )

    skill_val_style = ParagraphStyle(
        'SkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.4,
        textColor=TEXT_DARK
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("Filipe Vicente Hidalgo", title_style))
    story.append(Spacer(1, 1))
    story.append(Paragraph("Desenvolvedor Front-End React/Next.js &nbsp;|&nbsp; Suporte Técnico N2 SaaS &nbsp;|&nbsp; Customer Success Técnico", subtitle_style))
    story.append(Spacer(1, 1))

    contact_text = (
        "São Paulo, SP &bull; filipe_vicente@hotmail.com &bull; (11) 96615-2956<br/>"
        "LinkedIn: <a href='https://www.linkedin.com/in/filipevicentehidalgo' color='#0D9488'>linkedin.com/in/filipevicentehidalgo</a> &bull; "
        "GitHub: <a href='https://github.com/FilipeVicenteH' color='#0D9488'>github.com/FilipeVicenteH</a> &bull; "
        "Portfólio: <a href='https://filipevicenteh.vercel.app' color='#0D9488'>filipevicenteh.vercel.app</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 1))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceBefore=1, spaceAfter=2))

    # 2. RESUMO PROFISSIONAL
    story.append(Paragraph("RESUMO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))
    summary_p = (
        "<b>Desenvolvedor Front-End React/Next.js e Analista de Suporte Técnico N2</b> com mais de 2 anos de experiência no ecossistema SaaS e e-commerce. "
        "Especializado no desenvolvimento de aplicações web dinâmicas e responsivas (React, Next.js 15, TypeScript, Tailwind CSS), integrações via APIs RESTful e Webhooks, "
        "e resolução de chamados técnicos N2 com depuração detalhada de logs HTTP (Postman, Insomnia, cURL). "
        "Atuação destacada em Customer Success técnico, onboarding de lojistas, análise de churn/MRR e criação de dashboards em Power BI. "
        "Criador do sistema <b>UnicoCRM</b> para retenção de clientes e responsável pelo <b>Redesign UI/UX de 30 interfaces</b> da plataforma UnicoDrop. "
        "Dupla formação em Ciência da Computação (em conclusão) e Design Gráfico."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 1.5))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    skills_data = [
        [
            Paragraph("<b>Front-End & UI/UX:</b>", skill_label_style),
            Paragraph("React, Next.js 15 (App Router), TypeScript, JavaScript (ES6+), HTML5, CSS3, Tailwind CSS, Bootstrap, Figma, Design System", skill_val_style)
        ],
        [
            Paragraph("<b>Back-End & APIs:</b>", skill_label_style),
            Paragraph("Node.js, APIs RESTful, Webhooks HTTP, JSON Payloads, Prisma ORM, Neon PostgreSQL Cloud, SQL", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte Técnico N2:</b>", skill_label_style),
            Paragraph("Troubleshooting avançado, depuração de logs HTTP (Postman, Insomnia, cURL), Status Codes 4xx/5xx, gestão de chamados, suporte a SLAs", skill_val_style)
        ],
        [
            Paragraph("<b>Customer Success & Dados:</b>", skill_label_style),
            Paragraph("Onboarding técnico de lojistas, retenção de contas, análise de churn/MRR, parâmetros de gateway/frete, dashboards em Power BI e Excel", skill_val_style)
        ],
        [
            Paragraph("<b>Plataformas & Ferramentas:</b>", skill_label_style),
            Paragraph("Shopify, Nuvemshop, WhatsApp API/QR Code, Git, GitHub, Vercel Deploy, suporte a sistemas operacionais (Windows, Linux, macOS)", skill_val_style)
        ]
    ]

    t_skills = Table(skills_data, colWidths=[135, 421])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 1.5))

    # 4. PROJETOS RELEVANTES
    story.append(Paragraph("PROJETOS RELEVANTES", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    projects_list = [
        "<b>UnicoCRM &ndash; Gestão de Retenção & Reconversão de Churn (<a href='https://unico-crm.vercel.app/relatorios' color='#0D9488'>unico-crm.vercel.app</a>):</b> "
        "Desenvolvi uma aplicação SaaS Full-Stack em <b>Next.js 15 (App Router, Server Actions), TypeScript, Tailwind CSS, Prisma ORM e Neon PostgreSQL Cloud</b>. "
        "Estruturei relatórios de cancelamento, categorização por motivo de saída (preço, suporte, bugs) e pipeline de reativação. "
        "<i>Resultado: automação da régua de retenção e mitigação direta de perda de receita recorrente (MRR).</i>",

        "<b>UnicoDrop Redesign Visual & UI/UX &ndash; 30 interfaces codadas (<a href='https://telas-unico.vercel.app' color='#0D9488'>telas-unico.vercel.app</a>):</b> "
        "Liderei o redesign estético e funcional da plataforma, criando Design System no <b>Figma</b> e recodificando <b>30 telas operacionais em React, Tailwind CSS e ApexCharts</b> "
        "em 4 módulos (E-commerce, Dashboards, Mensageria e Configurações). "
        "<i>Resultado: otimização da usabilidade e redução estimada de 40% no tempo de localização de informações pelos lojistas.</i>",

        "<b>UnicoDrop Diagnóstico &ndash; Landing Page & Captação via Webhook (<a href='https://teste-web-hook.vercel.app' color='#0D9488'>teste-web-hook.vercel.app</a>):</b> "
        "Projetei e codifiquei landing page responsiva com fluxo interativo de auditoria em 7 perguntas, utilizando <b>HTML5, CSS3, JavaScript ES6+ e Webhooks HTTP</b>. "
        "Envia leads qualificados em tempo real para o CRM/Vendas. <i>Resultado: eliminação da triagem manual e aceleração da entrada de novos clientes.</i>"
    ]
    for proj_item in projects_list:
        story.append(Paragraph(f"&bull; {proj_item}", bullet_style))
    story.append(Spacer(1, 1.5))

    # 5. EXPERIÊNCIA PROFISSIONAL
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI, Desenvolvedor Front-End & Suporte N2 / CS Specialist", job_title_style)
    j1_company = Paragraph("Unico Drop", job_company_style)
    j1_period = Paragraph("08/2024 &ndash; Presente", job_period_style)

    header_table1 = Table([
        [j1_title, j1_period],
        [j1_company, Paragraph("", job_period_style)]
    ], colWidths=[396, 160])
    header_table1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table1)
    story.append(Spacer(1, 0.5))

    j1_bullets = [
        "Investiguei e resolvi chamados técnicos N2 de alta complexidade realizando depuração detalhada de payloads JSON, logs HTTP e requisições via <b>Postman, Insomnia e cURL</b>, garantindo a correção de falhas e o cumprimento rigoroso dos SLAs.",
        "Apoiei integrações entre a plataforma e e-commerces externos (<b>Shopify e Nuvemshop</b>), sincronizando pedidos, estoques e instâncias de mensageria automatizada (WhatsApp QR Code/API, SMS e e-mail).",
        "Conduzi o onboarding técnico de lojistas, configurando domínios customizados, pixels de conversão, tabelas de frete e gateways, além de criar dashboards operacionais em <b>Power BI e Excel</b> para suporte ao Customer Success, retenção de contas e mitigação de churn.",
        "Desenvolvi e mantive interfaces web e aplicações SaaS responsivas utilizando <b>React, Next.js 15, TypeScript, Tailwind CSS, Prisma ORM e Neon PostgreSQL Cloud</b>."
    ]
    for bullet in j1_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 1.2))

    # Job 2: Levlife
    j2_title = Paragraph("Design & Social Media Specialist | E-commerce", job_title_style)
    j2_company = Paragraph("Levlife", job_company_style)
    j2_period = Paragraph("03/2022 &ndash; 08/2023", job_period_style)

    header_table2 = Table([
        [j2_title, j2_period],
        [j2_company, Paragraph("", job_period_style)]
    ], colWidths=[396, 160])
    header_table2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table2)
    story.append(Spacer(1, 0.5))

    j2_bullets = [
        "Projetei e codifiquei landing pages responsivas e páginas de produtos otimizadas para conversão (CRO), aplicando técnicas de UI/UX, arquitetura de informação e prototipagem no <b>Figma</b> com estruturação em <b>HTML5, CSS3 e JavaScript ES6+</b>.",
        "Desenvolvi sistemas de identidade visual, banners promocionais e peças publicitárias para campanhas de tráfego pago utilizando <b>Figma, Photoshop e Illustrator</b>, impulsionando a presença digital da marca."
    ]
    for bullet in j2_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 1.2))

    # Job 3: 2º Tabelião
    j3_title = Paragraph("Auxiliar de Cartório & Atendimento Técnico", job_title_style)
    j3_company = Paragraph("2º Tabelião de Protestos e Notas de São Caetano do Sul", job_company_style)
    j3_period = Paragraph("05/2021 &ndash; 02/2022", job_period_style)

    header_table3 = Table([
        [j3_title, j3_period],
        [j3_company, Paragraph("", job_period_style)]
    ], colWidths=[396, 160])
    header_table3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table3)
    story.append(Spacer(1, 0.5))

    j3_bullets = [
        "Realizei atendimento técnico presencial e remoto a clientes corporativos, operando sistemas internos com foco na validação de dados, conferência minuciosa de documentos contratuais e otimização de fluxos operacionais em alto volume."
    ]
    for bullet in j3_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 1.5))

    # 6. FORMAÇÃO ACADÊMICA
    story.append(Paragraph("FORMAÇÃO ACADÊMICA", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    edu_data = [
        [
            Paragraph("<b>Bacharelado em Ciência da Computação</b> &ndash; <font color='#64748B'>Centro Universitário Descomplica (UniAmérica)</font>", skill_val_style),
            Paragraph("<font color='#64748B'>Conclusão: 07/2026</font>", job_period_style)
        ],
        [
            Paragraph("<b>Tecnólogo em Design Gráfico</b> &ndash; <font color='#64748B'>Faculdade Uninove</font>", skill_val_style),
            Paragraph("<font color='#64748B'>Concluído: 07/2020</font>", job_period_style)
        ]
    ]

    t_edu = Table(edu_data, colWidths=[396, 160])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 1.5))

    # 7. CERTIFICADOS, CURSOS E IDIOMAS
    story.append(Paragraph("CERTIFICADOS, CURSOS E IDIOMAS", section_heading_style))
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

    t_certs = Table(certs_data, colWidths=[278, 278])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    doc.build(story)

    # Check page count
    pdf_doc = fitz.open(output_filename)
    num_pages = len(pdf_doc)
    print(f"Generated PDF page count: {num_pages}")
    return num_pages

if __name__ == "__main__":
    out_dir = r"C:\Users\User\Desktop\Portfolio"
    out_file = os.path.join(out_dir, "Curriculo_Filipe_Vicente_Hidalgo.pdf")
    pages = create_resume(out_file)
    print(f"PDF generated at: {out_file} ({pages} page/s)")
