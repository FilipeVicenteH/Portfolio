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
        "<b>Analista de Segurança da Informação Júnior</b> com atuação focada em <b>Gestão de Identidades e Acessos (IAM)</b>, administração de privilégios em <b>Active Directory</b>, "
        "ambientes <b>Linux</b>, plataformas em nuvem (<b>Azure e AWS</b>) e governança de permissões em File Server. "
        "Experiência na operação do ciclo de vida de contas (concessão, alteração, revisão periódica e revogação de acessos), implementação de controles baseados em função (<b>RBAC</b>), "
        "segregação de funções (<b>SoD</b>) e suporte a evidências de auditoria de segurança da informação. "
        "Vivência consistente no atendimento de chamados N2 com rigoroso cumprimento de SLAs, depuração de logs HTTP, integração de sistemas SaaS e automações de processos. "
        "Dupla formação acadêmica em Ciência da Computação (em conclusão) e Design Gráfico."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 1.5))

    # 3. HABILIDADES TÉCNICAS
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    skills_data = [
        [
            Paragraph("<b>Gestão de Acessos & IAM:</b>", skill_label_style),
            Paragraph("Ciclo de vida de identidades, SailPoint IdentityIQ (operação/processos), RBAC, SoD (Segregação de Funções), governança de acessos, revisões periódicas, suporte a auditorias", skill_val_style)
        ],
        [
            Paragraph("<b>Diretórios & Ambientes:</b>", skill_label_style),
            Paragraph("Active Directory (usuários, grupos e permissões), File Server, Linux (permissões, grupos, chmod/chown), Windows Server, Azure AD / Entra ID, AWS IAM", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte N2 & Governança:</b>", skill_label_style),
            Paragraph("Troubleshooting de incidentes de acesso, chamados N2, depuração de logs HTTP (Postman, Insomnia, cURL), Status Codes 4xx/5xx, cumprimento de SLAs", skill_val_style)
        ],
        [
            Paragraph("<b>Automação & APIs:</b>", skill_label_style),
            Paragraph("JavaScript (ES6+), Python, APIs RESTful, Webhooks HTTP, JSON Payloads, Node.js, SQL, Git, GitHub, Vercel Deploy", skill_val_style)
        ],
        [
            Paragraph("<b>Ferramentas & BI:</b>", skill_label_style),
            Paragraph("Power BI (dashboards operacionais e relatórios de acesso), Excel avançado, Shopify, Nuvemshop, WhatsApp API", skill_val_style)
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
        "<b>UnicoCRM &ndash; Sistema de Governança, Controle de Acessos & Analytics (<a href='https://unico-crm.vercel.app/relatorios' color='#0D9488'>unico-crm.vercel.app</a>):</b> "
        "Desenvolvi aplicação SaaS em <b>Next.js 15 (App Router), TypeScript, Prisma ORM e Neon PostgreSQL Cloud</b>. "
        "Implementei controle de permissões por perfil (RBAC), trilhas de auditoria de chamados, categorização de motivos e painéis operacionais. "
        "<i>Resultado: automação da régua de atendimento e controle rigoroso de privilégios de acesso aos dados.</i>",

        "<b>UnicoDrop Diagnóstico &ndash; Fluxo de Auditoria & Validação de Acessos via Webhook (<a href='https://teste-web-hook.vercel.app' color='#0D9488'>teste-web-hook.vercel.app</a>):</b> "
        "Projetei e codifiquei interface de auditoria responsiva em 7 etapas com <b>HTML5, CSS3, JavaScript ES6+ e Webhooks HTTP</b> para validação e encaminhamento automatizado de dados em tempo real. "
        "<i>Resultado: eliminação da triagem manual e garantia de conformidade na entrada de registros.</i>"
    ]
    for proj_item in projects_list:
        story.append(Paragraph(f"&bull; {proj_item}", bullet_style))
    story.append(Spacer(1, 1.5))

    # 5. EXPERIÊNCIA PROFISSIONAL
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=2))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI, Suporte N2 & IAM Specialist", job_title_style)
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
        "Atuei na gestão do ciclo de vida de identidades e acessos (criação, alteração, revisão e revogação de permissões) de usuários em sistemas corporativos SaaS, Active Directory e diretórios de rede.",
        "Operei processos de concessão de acessos baseados em perfil (RBAC) e segregação de funções (SoD), atendendo chamados de suporte N2 com rigoroso cumprimento de SLAs e fornecimento de evidências para auditorias.",
        "Realizei a análise e depuração de logs HTTP, payloads JSON e requisições via <b>Postman, Insomnia e cURL</b> para diagnóstico de incidentes de permissão e integração de APIs RESTful e Webhooks (Shopify, Nuvemshop e WhatsApp API).",
        "Conduzi o onboarding técnico de lojistas, configurando domínios customizados, pixels e parâmetros de segurança, além de criar dashboards operacionais em <b>Power BI e Excel</b> para acompanhamento de acessos e indicadores corporativos."
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
        "Administrei privilégios de acesso e permissões de usuários em plataformas virtuais de e-commerce e sistemas digitais de venda.",
        "Projetei e codifiquei landing pages responsivas com <b>HTML5, CSS3, JavaScript e Figma</b>, garantindo a integridade dos dados e otimizando fluxos de conversão."
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
        "Realizei atendimento técnico presencial e remoto a clientes corporativos, operando sistemas internos com foco na validação de identidades, conferência minuciosa de documentos societários/contratuais e conformidade regulatória em alto volume."
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
