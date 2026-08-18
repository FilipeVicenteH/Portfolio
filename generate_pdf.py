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
    story.append(Paragraph("Analista de Engenharia de Software Júnior &nbsp;|&nbsp; Java & Spring Boot &nbsp;|&nbsp; React / Next.js & APIs REST", subtitle_style))
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
        "<b>Analista de Engenharia de Software Júnior</b> com sólida base em <b>Ciência da Computação</b> (em conclusão) e mais de 2 anos de experiência prática no "
        "desenvolvimento de software, sustentação de aplicações web/SaaS e suporte N2. "
        "Conhecimentos no desenvolvimento de soluções backend e APIs RESTful utilizando <b>Java (Spring Boot, Spring MVC, Spring Data)</b>, <b>Node.js</b>, "
        "<b>SQL (PostgreSQL, Oracle)</b> e documentação com <b>Swagger/OpenAPI</b>, integrados a interfaces modernas no frontend (<b>React, Next.js 15, TypeScript, Tailwind CSS</b>). "
        "Vivência no desenvolvimento de testes unitários e de integração (<b>JUnit</b>), depuração de incidentes em produção com análise de logs (<b>Log4j2, HTTP</b>), "
        "controle de versão com <b>Git/GitHub</b> e garantia de SLAs de sustentação. "
        "Dupla formação acadêmica com Bacharelado em Ciência da Computação e Tecnólogo em Design Gráfico."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 1.5))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    skills_data = [
        [
            Paragraph("<b>Linguagens & Backend:</b>", skill_label_style),
            Paragraph("Java (8+), JavaScript (ES6+), TypeScript, Node.js, Spring Framework (Spring Boot, Spring MVC, Spring Data), APIs RESTful, Webhooks, Swagger/OpenAPI", skill_val_style)
        ],
        [
            Paragraph("<b>Frontend & UI/UX:</b>", skill_label_style),
            Paragraph("React, Next.js 15 (App Router), HTML5, CSS3, Tailwind CSS, Bootstrap, Figma, Design System, usabilidade e componentização", skill_val_style)
        ],
        [
            Paragraph("<b>Bancos de Dados & SQL:</b>", skill_label_style),
            Paragraph("SQL, Oracle, PostgreSQL (Neon Cloud), Prisma ORM, modelagem de dados, consultas otimizadas e persistência", skill_val_style)
        ],
        [
            Paragraph("<b>Testes, Logs & Sustentação:</b>", skill_label_style),
            Paragraph("JUnit (testes unitários e de integração), Log4j2, depuração de logs HTTP (Postman, Insomnia, cURL), Status Codes 4xx/5xx, suporte N2, SLAs", skill_val_style)
        ],
        [
            Paragraph("<b>DevOps & Ferramentas:</b>", skill_label_style),
            Paragraph("Git, GitHub, Vercel Deploy, noções de Docker e CI/CD, ambientes Windows, Linux e macOS, inglês intermediário para documentação técnica", skill_val_style)
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
        "<b>UnicoCRM &ndash; Sistema SaaS Full-Stack de Gestão & Sustentação (<a href='https://unico-crm.vercel.app/relatorios' color='#0D9488'>unico-crm.vercel.app</a>):</b> "
        "Desenvolvi aplicação SaaS com <b>Next.js 15 (App Router, Server Actions), TypeScript, Tailwind CSS, Prisma ORM e PostgreSQL Cloud</b>. "
        "Implementei arquitetura de APIs RESTful, persistência em banco de dados, regras de negócio para relatórios operacionais e testes de integração. "
        "<i>Resultado: automação do fluxo de atendimento e estabilidade da solução em nuvem.</i>",

        "<b>UnicoDrop Redesign Visual & UI/UX &ndash; 30 interfaces codadas (<a href='https://telas-unico.vercel.app' color='#0D9488'>telas-unico.vercel.app</a>):</b> "
        "Liderei o redesign funcional de 30 telas em React e Tailwind CSS organizadas em 4 módulos operacionais, aplicando boas práticas de componentização e otimização. "
        "<i>Resultado: otimização da usabilidade e redução estimada em 40% no tempo de busca de informações.</i>",

        "<b>UnicoDrop Diagnóstico &ndash; Integração via Webhook & APIs (<a href='https://teste-web-hook.vercel.app' color='#0D9488'>teste-web-hook.vercel.app</a>):</b> "
        "Interface responsiva com fluxo interativo em 7 etapas desenvolvida com <b>HTML5, CSS3, JS assíncrono e consumo de Webhooks HTTP</b> para comunicação de dados em tempo real. "
        "<i>Resultado: automação da entrada de dados e eliminação de triagem manual.</i>"
    ]
    for proj_item in projects_list:
        story.append(Paragraph(f"&bull; {proj_item}", bullet_style))
    story.append(Spacer(1, 1.5))

    # 5. EXPERIÊNCIA PROFISSIONAL
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI, Desenvolvedor & Suporte N2", job_title_style)
    j1_company = Paragraph("Unico Drop", job_company_style)
    j1_period = Paragraph("08/2024 &ndash; 08/2026", job_period_style)

    header_table1 = Table([
        [j1_title, j1_period],
        [j1_company, Paragraph("São Paulo, SP", job_period_style)]
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
        "Atuei no desenvolvimento, evolução sistêmica e sustentação de aplicações SaaS, construindo e mantendo interfaces e integrações de dados com <b>React, Next.js 15, TypeScript, Tailwind CSS, Node.js e SQL</b>.",
        "Prestei suporte e sustentação N2 aos sistemas em produção, realizando troubleshooting avançado, depuração de erros com análise de logs (<b>Log4j2, logs HTTP</b>) e requisições via Postman/cURL para diagnóstico e resolução de incidentes.",
        "Atuei na integração de APIs RESTful e Webhooks com serviços externos (Shopify, Nuvemshop e APIs de mensageria), garantindo o tráfego seguro de JSON payloads e o cumprimento dos SLAs.",
        "Conduzi testes operacionais e onboarding técnico de clientes, além de construir dashboards no <b>Power BI e Excel</b> para visibilidade da estabilidade das aplicações."
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
        [j2_company, Paragraph("São Paulo, SP", job_period_style)]
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
        "Desenvolvi landing pages responsivas e componentes web com <b>HTML5, CSS3, JavaScript e Figma</b>, aplicando boas práticas de arquitetura de informação e usabilidade.",
        "Gerenciei configurações e integrações visuais em plataformas de e-commerce e sistemas digitais de venda."
    ]
    for bullet in j2_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 1.2))

    # Job 3: 2º Tabelião
    j3_title = Paragraph("Auxiliar de Atendimento Técnico & Análise Documental", job_title_style)
    j3_company = Paragraph("2º Tabelião de Protestos e Notas", job_company_style)
    j3_period = Paragraph("05/2021 &ndash; 02/2022", job_period_style)

    header_table3 = Table([
        [j3_title, j3_period],
        [j3_company, Paragraph("São Paulo, SP", job_period_style)]
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
        "Realizei atendimento técnico ao público e clientes corporativos, operando sistemas internos com foco na validação de dados, conferência minuciosa de documentos e otimização de fluxos de trabalho."
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
