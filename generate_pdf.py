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
    PRIMARY_COLOR = colors.HexColor('#0F172A')   # Navy
    SECONDARY_COLOR = colors.HexColor('#0D9488') # Teal Accent
    TEXT_DARK = colors.HexColor('#334155')       # Slate dark
    TEXT_MUTED = colors.HexColor('#64748B')      # Slate muted
    LINE_COLOR = colors.HexColor('#CBD5E1')      # Light border

    # Styles
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=21,
        textColor=PRIMARY_COLOR,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=11.5,
        textColor=SECONDARY_COLOR,
        alignment=TA_CENTER,
        spaceAfter=2
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=PRIMARY_COLOR,
        spaceBefore=5,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=11.5,
        textColor=PRIMARY_COLOR
    )

    job_company_style = ParagraphStyle(
        'JobCompany',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11,
        textColor=SECONDARY_COLOR
    )

    job_period_style = ParagraphStyle(
        'JobPeriod',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_MUTED,
        alignment=2 # Right
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=10.8,
        textColor=TEXT_DARK,
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=1
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=PRIMARY_COLOR
    )

    skill_val_style = ParagraphStyle(
        'SkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("Filipe Vicente Hidalgo", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Desenvolvedor Front-End &nbsp;|&nbsp; Suporte Técnico (N1/N2) &nbsp;|&nbsp; Customer Success", subtitle_style))
    story.append(Spacer(1, 1))

    contact_text = (
        "São Paulo, SP &bull; filipe_vicente@hotmail.com &bull; (11) 96615-2956<br/>"
        "<a href='https://www.linkedin.com/in/filipevicentehidalgo' color='#0D9488'>LinkedIn</a> &bull; "
        "<a href='https://github.com/FilipeVicenteH' color='#0D9488'>GitHub</a> &bull; "
        "<a href='https://www.behance.net/filipevicenteh' color='#0D9488'>Behance</a> &bull; "
        "<a href='https://filipevicenteh.vercel.app' color='#0D9488'>Portfólio Online</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceBefore=1, spaceAfter=4))

    # 2. RESUMO PROFISSIONAL
    story.append(Paragraph("RESUMO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))
    summary_p = (
        "Profissional com formação em <b>Ciência da Computação</b> e <b>Design Gráfico</b>, atuando em Suporte Técnico (N1/N2), "
        "integrações de sistemas (APIs e Webhooks), desenvolvimento Front-End (React, JavaScript) e Customer Success. "
        "Experiência no diagnóstico e resolução de incidentes técnicos, automação de fluxos operacionais (WhatsApp/E-mail), "
        "onboarding de clientes e criação de dashboards em Power BI. Perfil analítico e orientado a resultados, unindo capacidade técnica "
        "à visão de usabilidade e experiência do usuário (UX/UI)."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 3))

    # 3. HABILIDADES TÉCNICAS (Clean 2-Column Key-Value Table)
    story.append(Paragraph("HABILIDADES TÉCNICAS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

    skills_data = [
        [
            Paragraph("<b>Front-End:</b>", skill_label_style),
            Paragraph("HTML5, CSS3, JavaScript (ES6+), React, Tailwind CSS, Bootstrap", skill_val_style)
        ],
        [
            Paragraph("<b>Back-End & APIs:</b>", skill_label_style),
            Paragraph("Node.js, APIs RESTful, Webhooks, JSON", skill_val_style)
        ],
        [
            Paragraph("<b>Bancos de Dados & BI:</b>", skill_label_style),
            Paragraph("SQL, PostgreSQL, Oracle, Power BI, Excel Intermediário/Avançado", skill_val_style)
        ],
        [
            Paragraph("<b>Suporte & Operações:</b>", skill_label_style),
            Paragraph("Helpdesk N1/N2, Troubleshooting Técnico, Sistemas de Chamados, Suporte Remoto", skill_val_style)
        ],
        [
            Paragraph("<b>Integrações & E-commerce:</b>", skill_label_style),
            Paragraph("Shopify, Nuvemshop, Automações de Mensagens (WhatsApp, E-mail)", skill_val_style)
        ],
        [
            Paragraph("<b>Sistemas, Redes & Hardware:</b>", skill_label_style),
            Paragraph("Windows, Linux, macOS, TCP/IP, DNS, DHCP, Montagem & Manutenção de PCs", skill_val_style)
        ],
        [
            Paragraph("<b>Ferramentas & Design:</b>", skill_label_style),
            Paragraph("Git, GitHub, Figma, Photoshop, Illustrator", skill_val_style)
        ]
    ]

    t_skills = Table(skills_data, colWidths=[140, 400])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 3))

    # 4. HISTÓRICO PROFISSIONAL
    story.append(Paragraph("HISTÓRICO PROFISSIONAL", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

    # Job 1: Unico Drop
    j1_title = Paragraph("Analista de TI & Suporte Técnico", job_title_style)
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
        "Realizo atendimento técnico (N1/N2), solucionando incidentes operacionais e reduzindo o tempo de resposta (SLA) ao cliente.",
        "Investigo e corrijo falhas em integrações via API e Webhooks entre a plataforma e lojas virtuais (Shopify, Nuvemshop).",
        "Configuro automações de disparo de mensagens via WhatsApp e e-mail, criando e ajustando fluxos automatizados.",
        "Conduzo o onboarding de novos clientes e atuo em Customer Success, garantindo a retenção e adoção da plataforma.",
        "Desenvolvo melhorias no Front-End (HTML, CSS, JS, React) priorizando usabilidade e experiência do usuário (UX/UI).",
        "Construo dashboards no Power BI para análise de dados estratégicos e suporte à tomada de decisão."
    ]
    for bullet in j1_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # Job 2: Levlife
    j2_title = Paragraph("Design & Social Media | E-commerce", job_title_style)
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
        "Desenvolvi peças gráficas, conteúdos digitais e materiais visuais para fortalecer a presença da marca nas redes sociais.",
        "Criei landing pages com foco em engajamento, divulgação de produtos e conversão de clientes.",
        "Gerenciei e-commerce e plataformas digitais, apoiando a organização de produtos, conteúdos e campanhas.",
        "Planejei campanhas digitais e organizei conteúdos estratégicos para melhorar a comunicação da marca."
    ]
    for bullet in j2_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # Job 3: 2º Tabelião
    j3_title = Paragraph("Auxiliar de Cartório", job_title_style)
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
        "Realizei análise, conferência e organização de documentos em alto volume, garantindo agilidade e precisão interna.",
        "Prestei atendimento ao cliente e suporte administrativo, auxiliando na resolução de dúvidas e demandas operacionais.",
        "Otimizei fluxos internos com uso de sistemas e organização de processos, aumentando a eficiência operacional da equipe."
    ]
    for bullet in j3_bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 3))

    # 5. FORMAÇÃO ACADÊMICA
    story.append(Paragraph("FORMAÇÃO ACADÊMICA", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=1, spaceAfter=3))

    edu_data = [
        [
            Paragraph("<b>Bacharelado em Ciência da Computação</b> &ndash; <font color='#64748B'>Centro Universitário União das Américas Descomplica (UniAmérica)</font>", skill_val_style),
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
