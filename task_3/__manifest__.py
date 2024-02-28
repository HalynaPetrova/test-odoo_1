{
    'name': 'hr_hospital',
    'summary': '',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',
    
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '16.0.1.0.0',
    
    'depends': [
        "web",
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',

        'views/task_3_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/contact_person_views.xml',
        'views/diseas_catalog_views.xml',
        'views/visit_doctor_views.xml',
        'views/personal_doctor_history_views.xml',
        'report/diseas_catalog_report_templates.xml',
        'report/diseas_catalog_report.xml',
    ],
    'demo': [

    ],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 0,
    'currancy': 'EUR',

}