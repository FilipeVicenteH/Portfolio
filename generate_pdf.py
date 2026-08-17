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
    story.append(Paragraph("Analista de Segurança da Informação Júnior &nbsp;|&nbsp; IAM & Gestão de Acessos &nbsp;|&nbsp; Active Directory & Automação", subtitle_style))
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
        "<b>Analista de Segurança da Informação Júnior</b> com sólida base em <b>Ciência da Computação</b> (em conclusão) e mais de 2 anos de experiência prática em "
        "<b>Suporte Técnico N2</b>, sustentação de sistemas SaaS e administração de acessos de usuários. "
        "Conhecimentos em conceitos de <b>IAM (Gestão de Identidades e Acessos)</b>, ciclo de vida de contas (provisionamento, revisão e revogação), controle de acesso por função (<b>RBAC</b>), "
        "<b>Active Directory</b> (usuários, grupos e permissões), ambientes <b>Linux</b> e governança de acessos em File Server. "
        "Vivência no diagnóstico de incidentes de tecnologia, depuração de logs HTTP (Postman, Insomnia, cURL) e cumprimento de SLAs corporativos. "
        "Habilidade no desenvolvimento de automações e aplicações web (React, Next.js 15, JavaScript, APIs RESTful, SQL) e criação de dashboards em Power BI. "
        "Dupla formação acadêmica com Bacharelado em Ciência da Computação e Tecnólogo em Design Gráfico."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 1.5))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    skills_data = [
        [
            Paragraph("<b>Gestão de Identidades & IAM:</b>", skill_label_style),
            Paragraph("Ciclo de vida de identidades (provisionamento/revogação), RBAC, conceitos de SoD (Segregação de Funções), governança de acessos, revisões periódicas e evidências para auditoria de TI", skill_val_style)
        ],
        [
            Paragraph("<b>Diretórios & Ambientes:</b>", skill_label_style),
            Paragraph("Active Directory (gestão de usuários, grupos e permissões), File Server, permissões em Linux (usuários, grupos, chmod/chown), Windows Server e noções de IAM em nuvem (Azure/AWS)", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte Técnico N2 & SLAs:</b>", skill_label_style),
            Paragraph("Troubleshooting avançado de incidentes, depuração de logs HTTP (Postman, Insomnia, cURL), Status Codes 4xx/5xx, gestão de chamados operacionais e atendimento a SLAs", skill_val_style)
        ],
        [
            Paragraph("<b>Desenvolvimento & Automação:</b>", skill_label_style),
            Paragraph("JavaScript (ES6+), React, Next.js 15 (App Router), TypeScript, HTML5, CSS3, Tailwind CSS, APIs RESTful, Webhooks HTTP, JSON, Node.js, SQL, Git, GitHub", skill_val_style)
        ],
        [
            Paragraph("<b>Análise de Dados & BI:</b>", skill_label_style),
            Paragraph("Dashboards em Power BI e Excel avançado para acompanhamento de chamados, visibilidade de uso de ferramentas, métricas de retenção e relatórios gerenciais", skill_val_style)
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
        "<b>UnicoCRM &ndash; Sistema de Gestão & Painel Operacional (<a href='https://unico-crm.vercel.app/relatorios' color='#0D9488'>unico-crm.vercel.app</a>):</b> "
        "Desenvolvi aplicação SaaS Full-Stack em <b>Next.js 15 (App Router), TypeScript, Prisma ORM e Neon PostgreSQL Cloud</b>. "
        "Implementei controle de permissões de usuários, relatórios de ocorrências e histórico de atendimento. "
        "<i>Resultado: automação da régua de acompanhamento e organização de dados operacionais.</i>",

        "<b>UnicoDrop Redesign Visual & UI/UX &ndash; 30 interfaces codadas (<a href='https://telas-unico.vercel.app' color='#0D9488'>telas-unico.vercel.app</a>):</b> "
        "Liderei a reformulação visual da plataforma, criando Design System no <b>Figma</b> e recodificando <b>30 telas operacionais em React e Tailwind CSS</b> "
        "em 4 módulos (E-commerce, Dashboards, Mensageria e Configurações). "
        "<i>Resultado: otimização da usabilidade e redução estimada em 40% no tempo de busca de informações.</i>",

        "<b>UnicoDrop Diagnóstico &ndash; Fluxo de Auditoria via Webhook (<a href='https://teste-web-hook.vercel.app' color='#0D9488'>teste-web-hook.vercel.app</a>):</b> "
        "Projetei e codifiquei interface de auditoria em 7 etapas com <b>HTML5, CSS3, JavaScript ES6+ e Webhooks HTTP</b> para validação e encaminhamento de dados em tempo real. "
        "<i>Resultado: eliminação da triagem manual inicial.</i>"
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
        "Diagnostiquei e resolvi chamados técnicos N2 de alta complexidade, realizando depuração de logs HTTP, payloads JSON e requisições via <b>Postman, Insomnia e cURL</b> com foco no cumprimento de SLAs.",
        "Atuei no suporte à administração de contas, controle de acessos de lojistas e resolução de falhas em integrações com e-commerces (<b>Shopify e Nuvemshop</b>) e serviços de mensageria (WhatsApp QR Code/API, SMS e e-mail).",
        "Conduzi o onboarding técnico de lojistas, auxiliando na configuração de domínios customizados, pixels e parâmetros de segurança, além de estruturar dashboards operacionais em <b>Power BI e Excel</b> para suporte ao acompanhamento de métricas da plataforma.",
        "Desenvolvi e mantive aplicações e interfaces web responsivas utilizando <b>React, Next.js 15, TypeScript, Tailwind CSS, Prisma ORM e Neon PostgreSQL Cloud</b>."
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
        "Gerenciei permissões e acessos de usuários em plataformas de e-commerce e sistemas digitais de venda.",
        "Projetei e codifiquei landing pages responsivas e páginas de produto com <b>HTML5, CSS3, JavaScript e Figma</b>, além de criar identidades visuais e materiais institucionais no Photoshop e Illustrator."
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
        "Realizei atendimento técnico presencial e remoto a clientes corporativos, operando sistemas internos com foco na validação de dados, conferência minuciosa de documentos societários/contratuais e organização de fluxos operacionais em alto volume."
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
