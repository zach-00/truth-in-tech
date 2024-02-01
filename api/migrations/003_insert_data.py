steps = [
    [
        """
    INSERT INTO top_ten(salary, job_title, location, body, username, company_name, company_logo, date_created)
    VALUES
    (120000, 'Data Scientist', 'San Francisco, CA', 'Working as a data scientist at Google has been an incredible journey. The projects are intellectually stimulating, and the company culture fosters innovation and collaboration. The compensation and benefits are excellent, and the opportunities for growth are abundant.', 'ByteMaster87', 'Google LLC', 'https://www.gstatic.com/webp/gallery/1.jpg', '2024-01-26'),
    (130000, 'Software Engineer', 'Seattle, WA', 'Amazon provides software engineers with an environment that encourages ownership and innovation. The projects are challenging, and the resources available for development are top-notch. The compensation and benefits package is competitive, and the company values work-life balance.', 'CodeNinjaX', 'Amazon.com, Inc.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1280px-Amazon_logo.svg.png', '2024-01-25'),
    (125000, 'Product Manager', 'Menlo Park, CA', 'Meta (formerly Facebook) offers product managers the opportunity to work on products that impact billions of lives. The work environment is dynamic, and the company values creativity and innovation. The compensation and benefits are generous, and the culture encourages personal and professional growth.', 'QuantumGeek23', 'Meta (formerly Facebook)', 'https://www.facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png', '2024-01-24'),
    (135000, 'Machine Learning Engineer', 'Mountain View, CA', 'Apple provides machine learning engineers with the opportunity to work on cutting-edge technologies that shape the future. The culture of excellence permeates every aspect of the work environment, and the projects are both challenging and rewarding. The compensation and benefits package is among the best in the industry.', 'BinaryByteBot', 'Apple Inc.', 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg', '2024-01-23'),
    (120000, 'Network Engineer', 'Redmond, WA', 'Microsoft offers network engineers a platform to work on some of the most complex and innovative networking solutions. The company culture promotes collaboration and continuous learning, and the compensation package is competitive. The opportunities for career growth are vast, making it an exciting place to work.', 'PixelPioneer99', 'Microsoft Corporation', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/1280px-Microsoft_logo.svg.png', '2024-01-22'),
    (130000, 'Cybersecurity Analyst', 'San Francisco, CA', 'Twitter values cybersecurity analysts and provides them with the resources needed to protect the platform and its users. The work environment is fast-paced and dynamic, and the projects are intellectually challenging. The compensation and benefits package is competitive, and the company culture encourages work-life balance.', 'TechWhizKid', 'Twitter, Inc.', 'https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Twitter_Logo_as_of_2021.svg/1280px-Twitter_Logo_as_of_2021.svg.png', '2024-01-21'),
    (125000, 'Cloud Solutions Architect', 'Palo Alto, CA', 'LinkedIn offers cloud solutions architects the opportunity to work on innovative solutions that drive business success. The company culture fosters collaboration and creativity, and the compensation package is competitive. The leadership team is supportive, and the work environment encourages continuous learning and growth.', 'CyborgCoder42', 'LinkedIn Corporation', 'https://logos-download.com/wp-content/uploads/2016/03/LinkedIn_Logo_2019.png', '2024-01-20'),
    (130000, 'Data Engineer', 'San Francisco, CA', 'Uber provides data engineers with the opportunity to work on large-scale data infrastructure projects that power its platform. The work environment is dynamic and fast-paced, and the projects are intellectually stimulating. The compensation and benefits package is competitive, and the company culture encourages innovation and collaboration.', 'DataDynamo9000', 'Uber Technologies, Inc.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Uber_logo_2018.svg/1200px-Uber_logo_2018.svg.png', '2024-01-19'),
    (120000, 'DevOps Engineer', 'Santa Clara, CA', 'NVIDIA offers devops engineers the chance to work with state-of-the-art technologies in a dynamic and fast-paced environment. The company fosters a culture of innovation and encourages employees to push boundaries. The compensation and benefits package is competitive, and the opportunities for career advancement are abundant.', 'SiliconSorcerer', 'NVIDIA Corporation', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Nvidia_logo.svg/1280px-Nvidia_logo.svg.png', '2024-01-18'),
    (125000, 'UI/UX Designer', 'San Jose, CA', 'Cisco empowers UI/UX designers to create intuitive and engaging user experiences for its products and services. The company values creativity and encourages designers to push the boundaries of innovation. The compensation and benefits package is competitive, and the culture of collaboration and inclusivity fosters creativity and personal growth.', 'AlgorithmAce', 'Cisco Systems, Inc.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Cisco_logo.svg/1280px-Cisco_logo.svg.png', '2024-01-17');
        """,
        """
        """,
    ],
    [
        """
    INSERT INTO companies (company_name, company_logo) VALUES
    ('Google', 'https://play-lh.googleusercontent.com/1-hPxafOxdYpYZEOKzNIkSP43HXCNftVJVttoo4ucl7rsMASXW3Xr6GlXURCubE1tA=w3840-h2160-rw'),
    ('Apple', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Apple_Computer_Logo_rainbow.svg/1757px-Apple_Computer_Logo_rainbow.svg.png'),
    ('Microsoft', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Microsoft_logo_%282012%29.svg/2560px-Microsoft_logo_%282012%29.svg.png'),
    ('Amazon', 'https://m.media-amazon.com/images/G/01/gc/designs/livepreview/a_generic_white_10_us_noto_email_v2016_us-main._CB627448186_.png'),
    ('Facebook', 'https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg'),
    ('Tencent', 'https://1000logos.net/wp-content/uploads/2018/08/Tencent-Logo.png'),
    ('Tesla', 'https://1000logos.net/wp-content/uploads/2018/02/Font-Tesla-logo.jpg'),
    ('Samsung Electronics', 'https://www.shutterstock.com/image-vector/samsung-logo-icon-south-korean-260nw-2269709285.jpg'),
    ('Intel', 'https://www.freeiconspng.com/thumbs/intel-logo-png/intel-logo-png-2.png'),
    ('IBM', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/1024px-IBM_logo.svg.png'),
    ('Oracle', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Oracle_logo.svg/2560px-Oracle_logo.svg.png'),
    ('Cisco Systems', 'https://i.pinimg.com/736x/e8/21/69/e8216982516dda4166f45d0606cd3264.jpg'),
    ('Adobe Inc.', 'https://1000logos.net/wp-content/uploads/2021/04/Adobe-logo.png'),
    ('NVIDIA', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/NVIDIA_logo.svg/2560px-NVIDIA_logo.svg.png'),
    ('Salesforce', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Salesforce.com_logo.svg/2560px-Salesforce.com_logo.svg.png'),
    ('Accenture', 'https://www.smartglobalgovernance.com/wp-content/uploads/Accenture-2.svg'),
    ('Sony', 'https://upload.wikimedia.org/wikipedia/commons/c/ca/Sony_logo.svg'),
    ('HP Inc.', 'https://www.shutterstock.com/image-photo/siegen-nrw-germany-23-08-260nw-2352562821.jpg'),
    ('Dell Technologies', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Dell_Logo.png/799px-Dell_Logo.png'),
    ('VMware', 'https://upload.wikimedia.org/wikipedia/commons/1/11/VMware_logo.svg'),
    ('Uber Technologies', 'https://helios-i.mashable.com/imagery/articles/03y6VwlrZqnsuvnwR8CtGAL/hero-image.fill.size_1200x675.v1623372852.jpg'),
    ('Twitter', 'https://static.dezeen.com/uploads/2023/07/x-logo-twitter-elon-musk_dezeen_2364_col_0-1.jpg'),
    ('Netflix', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Netflix_2015_logo.svg/1024px-Netflix_2015_logo.svg.png'),
    ('PayPal', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/PayPal.svg/2560px-PayPal.svg.png'),
    ('Snap Inc.', 'https://1000logos.net/wp-content/uploads/2017/07/Snapchat-Logo-color.jpg'),
    ('Qualcomm', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Qualcomm-Logo.svg/2560px-Qualcomm-Logo.svg.png'),
    ('Square, Inc.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Square%2C_Inc._logo.svg/2560px-Square%2C_Inc._logo.svg.png'),
    ('Project Babbage', 'https://projectbabbage.com/assets/images/babblogo4.svg'),
    ('Booking Holdings', 'https://download.logo.wine/logo/Booking_Holdings/Booking_Holdings-Logo.wine.png'),
    ('Baidu', 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Baidu.svg/1280px-Baidu.svg.png');
        """,
        """
        """,
    ],
]
