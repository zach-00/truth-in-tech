steps = [
    [
        """
    INSERT INTO top_ten(salary, job_title, location, body, username, company_name, company_logo, date_created)
    VALUES
    (120000, 'Data Scientist', 'San Francisco, CA', 'Working as a data scientist at Google has been an incredible journey. The projects are intellectually stimulating, and the company culture fosters innovation and collaboration. The compensation and benefits are excellent, and the opportunities for growth are abundant.', 'ByteMaster87', 'Google LLC', 'https://play-lh.googleusercontent.com/1-hPxafOxdYpYZEOKzNIkSP43HXCNftVJVttoo4ucl7rsMASXW3Xr6GlXURCubE1tA=w3840-h2160-rw', '2024-01-26'),
    (130000, 'Software Engineer', 'Seattle, WA', 'Amazon provides software engineers with an environment that encourages ownership and innovation. The projects are challenging, and the resources available for development are top-notch. The compensation and benefits package is competitive, and the company values work-life balance.', 'CodeNinjaX', 'Amazon.com, Inc.', 'https://m.media-amazon.com/images/G/01/gc/designs/livepreview/a_generic_white_10_us_noto_email_v2016_us-main._CB627448186_.png', '2024-01-25'),
    (125000, 'Product Manager', 'Menlo Park, CA', 'Meta (formerly Facebook) offers product managers the opportunity to work on products that impact billions of lives. The work environment is dynamic, and the company values creativity and innovation. The compensation and benefits are generous, and the culture encourages personal and professional growth.', 'QuantumGeek23', 'Meta (formerly Facebook)', 'https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg', '2024-01-24'),
    (135000, 'Machine Learning Engineer', 'Mountain View, CA', 'Apple provides machine learning engineers with the opportunity to work on cutting-edge technologies that shape the future. The culture of excellence permeates every aspect of the work environment, and the projects are both challenging and rewarding. The compensation and benefits package is among the best in the industry.', 'BinaryByteBot', 'Apple Inc.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Apple_Computer_Logo_rainbow.svg/1757px-Apple_Computer_Logo_rainbow.svg.png', '2024-01-23'),
    (120000, 'Network Engineer', 'Redmond, WA', 'Microsoft offers network engineers a platform to work on some of the most complex and innovative networking solutions. The company culture promotes collaboration and continuous learning, and the compensation package is competitive. The opportunities for career growth are vast, making it an exciting place to work.', 'PixelPioneer99', 'Microsoft Corporation', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Microsoft_logo_%282012%29.svg/2560px-Microsoft_logo_%282012%29.svg.png', '2024-01-22'),
    (130000, 'Cybersecurity Analyst', 'San Francisco, CA', 'Twitter values cybersecurity analysts and provides them with the resources needed to protect the platform and its users. The work environment is fast-paced and dynamic, and the projects are intellectually challenging. The compensation and benefits package is competitive, and the company culture encourages work-life balance.', 'TechWhizKid', 'Twitter, Inc.', 'https://static.dezeen.com/uploads/2023/07/x-logo-twitter-elon-musk_dezeen_2364_col_0-1.jpg', '2024-01-21'),
    (125000, 'Cloud Solutions Architect', 'Palo Alto, CA', 'LinkedIn offers cloud solutions architects the opportunity to work on innovative solutions that drive business success. The company culture fosters collaboration and creativity, and the compensation package is competitive. The leadership team is supportive, and the work environment encourages continuous learning and growth.', 'CyborgCoder42', 'LinkedIn Corporation', 'https://i0.wp.com/www.alphr.com/wp-content/uploads/2023/08/1637655738-linkedin-101-hero2x.jpg?resize=738%2C320&ssl=1', '2024-01-20'),
    (130000, 'Data Engineer', 'San Francisco, CA', 'Uber provides data engineers with the opportunity to work on large-scale data infrastructure projects that power its platform. The work environment is dynamic and fast-paced, and the projects are intellectually stimulating. The compensation and benefits package is competitive, and the company culture encourages innovation and collaboration.', 'DataDynamo9000', 'Uber Technologies, Inc.', 'https://helios-i.mashable.com/imagery/articles/03y6VwlrZqnsuvnwR8CtGAL/hero-image.fill.size_1200x675.v1623372852.jpg', '2024-01-19'),
    (120000, 'DevOps Engineer', 'Santa Clara, CA', 'NVIDIA offers devops engineers the chance to work with state-of-the-art technologies in a dynamic and fast-paced environment. The company fosters a culture of innovation and encourages employees to push boundaries. The compensation and benefits package is competitive, and the opportunities for career advancement are abundant.', 'SiliconSorcerer', 'NVIDIA Corporation', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/NVIDIA_logo.svg/2560px-NVIDIA_logo.svg.png', '2024-01-18'),
    (125000, 'UI/UX Designer', 'San Jose, CA', 'Cisco empowers UI/UX designers to create intuitive and engaging user experiences for its products and services. The company values creativity and encourages designers to push the boundaries of innovation. The compensation and benefits package is competitive, and the culture of collaboration and inclusivity fosters creativity and personal growth.', 'AlgorithmAce', 'Cisco Systems, Inc.', 'https://i.pinimg.com/736x/e8/21/69/e8216982516dda4166f45d0606cd3264.jpg', '2024-01-17');
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
    [
        """
    INSERT INTO accounts (username, first_name, last_name, hashed_password, email) VALUES
    ('TruthInTech', 'John', 'Doe', '$2b$12$nkCjXX1I3QFLY.cMoZ7StOdqKRebPgYTE1vxGjlIpfqUr5xMjpA4K', 'john.doe@example.com'),
    ('GeekMaster', 'Alice', 'Smith', '$2b$12$randomhashedpassword', 'alice.smith@example.com'),
    ('CodeNinja', 'Bob', 'Johnson', '$2b$12$randomhashedpassword', 'bob.johnson@example.com'),
    ('TechWhiz', 'Emma', 'Brown', '$2b$12$randomhashedpassword', 'emma.brown@example.com'),
    ('ByteWizard', 'David', 'Miller', '$2b$12$randomhashedpassword', 'david.miller@example.com'),
    ('CyberGenius', 'Olivia', 'Wilson', '$2b$12$randomhashedpassword', 'olivia.wilson@example.com'),
    ('PixelPirate', 'James', 'Taylor', '$2b$12$randomhashedpassword', 'james.taylor@example.com'),
    ('LogicLord', 'Emily', 'Anderson', '$2b$12$randomhashedpassword', 'emily.anderson@example.com'),
    ('DataDiva', 'Daniel', 'Thomas', '$2b$12$randomhashedpassword', 'daniel.thomas@example.com'),
    ('NetNinja', 'Sophia', 'Roberts', '$2b$12$randomhashedpassword', 'sophia.roberts@example.com'),
    ('WebWizard', 'Michael', 'Clark', '$2b$12$randomhashedpassword', 'michael.clark@example.com'),
    ('TechieGuru', 'Grace', 'Hall', '$2b$12$randomhashedpassword', 'grace.hall@example.com'),
    ('CodeCrusader', 'William', 'Lewis', '$2b$12$randomhashedpassword', 'william.lewis@example.com'),
    ('DataDynamo', 'Charlotte', 'Walker', '$2b$12$randomhashedpassword', 'charlotte.walker@example.com'),
    ('ByteBandit', 'Benjamin', 'Young', '$2b$12$randomhashedpassword', 'benjamin.young@example.com'),
    ('TechTitan', 'Ava', 'Green', '$2b$12$randomhashedpassword', 'ava.green@example.com'),
    ('CyberChampion', 'Mason', 'Harris', '$2b$12$randomhashedpassword', 'mason.harris@example.com'),
    ('PixelProphet', 'Lily', 'King', '$2b$12$randomhashedpassword', 'lily.king@example.com');
        """,
        """
        """,
    ],
    [
        """
    INSERT INTO reviews (anonymous, salary, job_title, location, body, account_id, company_id)
    VALUES
        (FALSE, 80000, 'Software Engineer', 'San Francisco, CA', 'Working at a tech company in San Francisco has been an amazing experience. The fast-paced environment and collaborative culture make every day exciting. The opportunities for growth and innovation are endless.', 4, 1),
        (TRUE, 90000, 'Data Scientist', 'Seattle, WA', 'As a data scientist in Seattle, I appreciate the work-life balance and the emphasis on innovation. The company fosters a supportive environment where employees are encouraged to explore new ideas.', 8, 4),
        (FALSE, 75000, 'Product Manager', 'Austin, TX', 'Austin is a vibrant city for tech, and working as a product manager here has been rewarding. The company values creativity and initiative, which allows me to make a real impact.', 11, 4),
        (TRUE, 85000, 'Software Developer', 'Boston, MA', 'Working as a software developer in Boston has been a fulfilling experience. The tech scene here is dynamic and diverse, and I have had the opportunity to work on cutting-edge projects.', 6, 2),
        (FALSE, 82000, 'UX Designer', 'New York City, NY', 'New York City is a hub for innovation, and working as a UX designer here has been exhilarating. The company encourages creativity and provides ample opportunities for professional growth.', 14, 7),
        (TRUE, 88000, 'Systems Engineer', 'San Jose, CA', 'As a systems engineer in San Jose, I am surrounded by some of the brightest minds in the industry. The collaborative environment and access to cutting-edge technology make every day rewarding.', 17, 4),
        (FALSE, 78000, 'Network Administrator', 'Denver, CO', 'Denver offers a perfect blend of tech opportunities and outdoor activities. As a network administrator, I appreciate the work-life balance and the supportive community.', 8, 11),
        (TRUE, 92000, 'Data Analyst', 'Austin, TX', 'Austin tech scene is thriving, and as a data analyst, I have had the chance to work on challenging projects that drive innovation. The company culture fosters collaboration and continuous learning.', 1, 13),
        (FALSE, 76000, 'Quality Assurance Engineer', 'Raleigh, NC', 'Raleigh tech community is vibrant and inclusive. As a QA engineer, I have had the opportunity to contribute to the development of cutting-edge products while enjoying the city rich cultural scene.', 2, 15),
        (TRUE, 93000, 'Software Architect', 'San Francisco, CA', 'San Francisco is a hotbed for tech innovation, and as a software architect, I have been privileged to work on groundbreaking projects that push the boundaries of technology.', 3, 17),
        (FALSE, 110000, 'Software Engineer', 'Mountain View, CA', 'Working at Google is a dream come true. The innovative projects, supportive culture, and amazing perks make it an exceptional place to work. I feel challenged and inspired every day.', 7, 1),
        (TRUE, 100000, 'Data Scientist', 'San Francisco, CA', 'Google commitment to innovation is truly remarkable. As a data scientist, I have had the opportunity to work with cutting-edge technology and collaborate with brilliant minds from around the world.', 10, 1),
        (FALSE, 95000, 'Product Manager', 'Seattle, WA', 'Being a product manager at Google is both exhilarating and rewarding. The company dedication to creating impactful products and fostering a culture of continuous learning sets it apart.', 13, 1),
        (TRUE, 120000, 'Software Developer', 'Cupertino, CA', 'Apple culture of innovation and attention to detail is unparalleled. As a software developer, I have had the privilege to work on products that redefine the industry standards.', 16, 2),
        (FALSE, 115000, 'UX Designer', 'San Francisco, CA', 'Apple commitment to user experience is evident in every project. As a UX designer, I have been challenged to think creatively and push the boundaries of design.', 4, 2),
        (TRUE, 105000, 'Systems Engineer', 'Austin, TX', 'Apple dedication to quality and performance sets it apart. As a systems engineer, I have had the opportunity to contribute to products that have a real impact on people lives.', 5, 2),
        (FALSE, 125000, 'Software Engineer', 'Redmond, WA', 'Microsoft culture of empowerment and innovation fosters creativity and collaboration. As a software engineer, I have had the opportunity to work on projects that shape the future of technology.', 6, 3),
        (TRUE, 115000, 'Data Scientist', 'Seattle, WA', 'Microsoft commitment to AI and machine learning is inspiring. As a data scientist, I have been able to explore cutting-edge techniques and apply them to real-world problems.', 7, 4),
        (FALSE, 110000, 'Product Manager', 'Redmond, WA', 'Being a product manager at Microsoft is both challenging and rewarding. The company focus on user-centric design and innovation creates an environment where every idea counts.', 8, 6),
        (TRUE, 130000, 'Software Developer', 'Seattle, WA', 'Amazon customer-centric culture drives innovation and growth. As a software developer, I have had the opportunity to work on projects that impact millions of customers worldwide.', 9, 4),
        (FALSE, 120000, 'UX Designer', 'San Francisco, CA', 'Amazon focus on user experience sets it apart in the industry. As a UX designer, I have been able to create intuitive and seamless experiences that delight customers.', 10, 4),
        (TRUE, 110000, 'Systems Engineer', 'Arlington, VA', 'Amazon commitment to innovation and technology is unparalleled. As a systems engineer, I have had the chance to work on projects that are at the forefront of cloud computing.', 11, 4),
        (FALSE, 135000, 'Software Engineer', 'Menlo Park, CA', 'Facebook mission to connect the world is inspiring. As a software engineer, I have been able to work on projects that have a meaningful impact on people lives.', 12, 8),
        (TRUE, 125000, 'Data Scientist', 'San Francisco, CA', 'Facebook data-driven culture fosters innovation and creativity. As a data scientist, I have had the opportunity to analyze vast amounts of data and derive valuable insights.', 13, 8),
        (FALSE, 115000, 'Product Manager', 'Menlo Park, CA', 'Being a product manager at Facebook is both challenging and rewarding. The company focus on user experience and innovation creates an environment where ideas flourish.', 14, 8),
        (TRUE, 140000, 'Software Developer', 'Shenzhen, China', 'Tencent commitment to innovation and technology is unmatched. As a software developer, I have had the opportunity to work on projects that redefine the digital landscape.', 15, 6),
        (FALSE, 130000, 'UX Designer', 'Shenzhen, China', 'Tencent user-centric design philosophy sets it apart in the industry. As a UX designer, I have been able to create engaging and intuitive experiences for millions of users.', 16, 6),
        (TRUE, 120000, 'Systems Engineer', 'Shenzhen, China', 'Tencent culture of collaboration and innovation makes it an exciting place to work. As a systems engineer, I have had the opportunity to tackle complex challenges and drive technological advancements.', 17, 6),
        (FALSE, 145000, 'Software Engineer', 'Palo Alto, CA', 'Tesla mission to accelerate the world transition to sustainable energy is inspiring. As a software engineer, I have had the opportunity to work on groundbreaking projects that push the boundaries of innovation.', 18, 7),
        (TRUE, 135000, 'Data Scientist', 'Fremont, CA', 'Tesla data-driven approach to innovation sets it apart in the automotive industry. As a data scientist, I have been able to analyze complex data sets and contribute to the development of cutting-edge technologies.', 1, 7),
        (FALSE, 125000, 'Product Manager', 'Palo Alto, CA', 'Being a product manager at Tesla is both challenging and rewarding. The company commitment to innovation and sustainability creates an environment where every idea matters.', 1, 7),
        (TRUE, 150000, 'Software Developer', 'Seoul, South Korea', 'Samsung dedication to innovation and quality is evident in every product. As a software developer, I have had the opportunity to work on projects that push the boundaries of technology.', 3, 8),
        (FALSE, 140000, 'UX Designer', 'Seoul, South Korea', 'Samsung user-centric design philosophy drives innovation and creativity. As a UX designer, I have been able to create meaningful experiences that enhance the lives of millions of users.', 4, 8),
        (TRUE, 130000, 'Systems Engineer', 'Seoul, South Korea', 'Samsung culture of collaboration and excellence makes it an exciting place to work. As a systems engineer, I have had the opportunity to work on cutting-edge projects that shape the future of technology.', 5, 8),
        (FALSE, 85000, 'Software Engineer', 'San Francisco, CA', 'Working at Google has been a dream come true. The company commitment to innovation and the collaborative environment make it an exciting place to work. I have had the opportunity to work on cutting-edge projects that have a global impact.', 4, 1),
        (TRUE, 90000, 'iOS Developer', 'Cupertino, CA', 'Apple is more than just a company; it a culture of excellence and innovation. As an iOS developer, I have been privileged to contribute to products that redefine the industry. The attention to detail and commitment to quality are unparalleled.', 8, 2),
        (FALSE, 80000, 'Software Engineer', 'Redmond, WA', 'Joining Microsoft has been a transformative experience. The company focus on empowering employees and fostering creativity has allowed me to grow both personally and professionally. Working here feels like being part of something bigger than myself.', 11, 6),
        (TRUE, 95000, 'Software Developer', 'Seattle, WA', 'Amazon is at the forefront of innovation, and working here has been both challenging and rewarding. The fast-paced environment and emphasis on customer obsession have pushed me to excel and grow as a professional.', 3, 4),
        (FALSE, 90000, 'Software Engineer', 'Menlo Park, CA', 'Facebook mission to connect the world is evident in every aspect of its culture. Working here has been a journey of continuous learning and growth. The company commitment to impact and innovation inspires me every day.', 6, 4),
        (TRUE, 85000, 'Software Engineer', 'Shenzhen, China', 'Tencent commitment to innovation and user experience is unparalleled. As a software engineer, I have had the opportunity to work on projects that reach millions of users worldwide. The company culture fosters creativity and collaboration.', 9, 6),
        (FALSE, 88000, 'Software Engineer', 'Palo Alto, CA', 'Tesla vision for the future is both ambitious and inspiring. Working here has allowed me to be part of something truly revolutionary. The fast-paced environment and culture of innovation make every day exciting.', 3, 7),
        (TRUE, 82000, 'Hardware Engineer', 'Seoul, South Korea', 'Samsung Electronics is synonymous with quality and innovation. As a hardware engineer, I have had the privilege of contributing to products that shape the future of technology. The company commitment to excellence is unmatched.', 3, 8),
        (FALSE, 78000, 'Software Engineer', 'Santa Clara, CA', 'Joining Intel has been a career-defining experience. The company legacy of innovation and commitment to pushing the boundaries of technology have inspired me to reach new heights. Working here feels like being part of a community that drives progress.', 8, 6),
        (TRUE, 91000, 'Software Developer', 'Armonk, NY', 'IBM dedication to innovation and problem-solving is unparalleled. As a software developer, I have had the opportunity to work on projects that tackle some of the world most pressing challenges. The company culture fosters collaboration and continuous learning.', 4, 10),
        (FALSE, 85000, 'Software Engineer', 'San Francisco, CA', 'Working at Google has been a dream come true. The company commitment to innovation and the collaborative environment make it an exciting place to work. I have had the opportunity to work on cutting-edge projects that have a global impact.', 6, 1),
        (TRUE, 90000, 'iOS Developer', 'Cupertino, CA', 'Apple is more than just a company; it a culture of excellence and innovation. As an iOS developer, I have been privileged to contribute to products that redefine the industry. The attention to detail and commitment to quality are unparalleled.', 8, 2),
        (FALSE, 80000, 'Software Engineer', 'Redmond, WA', 'Joining Microsoft has been a transformative experience. The company focus on empowering employees and fostering creativity has allowed me to grow both personally and professionally. Working here feels like being part of something bigger than myself.', 11, 8),
        (TRUE, 95000, 'Software Developer', 'Seattle, WA', 'Amazon is at the forefront of innovation, and working here has been both challenging and rewarding. The fast-paced environment and emphasis on customer obsession have pushed me to excel and grow as a professional.', 3, 4),
        (FALSE, 90000, 'Software Engineer', 'Menlo Park, CA', 'Facebook mission to connect the world is evident in every aspect of its culture. Working here has been a journey of continuous learning and growth. The company commitment to impact and innovation inspires me every day.', 6, 6),
        (TRUE, 85000, 'Software Engineer', 'Shenzhen, China', 'Tencent commitment to innovation and user experience is unparalleled. As a software engineer, I have had the opportunity to work on projects that reach millions of users worldwide. The company culture fosters creativity and collaboration.', 9, 6),
        (FALSE, 88000, 'Software Engineer', 'Palo Alto, CA', 'Tesla vision for the future is both ambitious and inspiring. Working here has allowed me to be part of something truly revolutionary. The fast-paced environment and culture of innovation make every day exciting.', 3, 7),
        (TRUE, 82000, 'Hardware Engineer', 'Seoul, South Korea', 'Samsung Electronics is synonymous with quality and innovation. As a hardware engineer, I have had the privilege of contributing to products that shape the future of technology. The company commitment to excellence is unmatched.', 3, 8),
        (FALSE, 78000, 'Software Engineer', 'Santa Clara, CA', 'Joining Intel has been a career-defining experience. The company legacy of innovation and commitment to pushing the boundaries of technology have inspired me to reach new heights. Working here feels like being part of a community that drives progress.', 3, 8),
        (TRUE, 91000, 'Software Developer', 'Armonk, NY', 'IBM dedication to innovation and problem-solving is unparalleled. As a software developer, I have had the opportunity to work on projects that tackle some of the world most pressing challenges. The company culture fosters collaboration and continuous learning.', 4, 10),
        (FALSE, 90000, 'Software Engineer', 'Redwood City, CA', 'Working at Oracle has been an incredible experience. The company commitment to innovation and cutting-edge technology is evident in everything we do. The opportunities for growth and impact are endless, and I am proud to be part of such an amazing team.', 4, 11),
        (TRUE, 85000, 'Network Engineer', 'San Jose, CA', 'Cisco Systems is a global leader in networking technology, and working here has been both challenging and rewarding. The collaborative culture and emphasis on innovation make every day exciting. I have had the opportunity to work on projects that shape the future of networking.', 7, 12),
        (FALSE, 80000, 'Software Developer', 'San Jose, CA', 'Joining Adobe has been a career-defining decision. The company commitment to creativity and innovation is inspiring. As a software developer, I have had the opportunity to work on projects that push the boundaries of digital experiences.', 5, 13),
        (TRUE, 87000, 'Graphics Engineer', 'Santa Clara, CA', 'NVIDIa dedication to pushing the boundaries of graphics technology is unmatched. Working here has been a thrilling experience filled with opportunities to innovate and create groundbreaking solutions. The company culture of excellence drives me to achieve my best every day.', 6, 15),
        (FALSE, 82000, 'Sales Representative', 'San Francisco, CA', 'Salesforce is more than just a company; it a community of trailblazers committed to making a difference. As a sales representative, I have had the opportunity to work with inspiring clients and be part of projects that transform businesses.', 6, 16),
        (TRUE, 92000, 'Consultant', 'New York City, NY', 'Accenture dedication to delivering innovative solutions is truly remarkable. Working here has been an incredible journey of growth and learning. The collaborative environment and diverse projects have allowed me to expand my skills and make a real impact.', 8, 17),
        (FALSE, 85000, 'Software Engineer', 'Tokyo, Japan', 'Sony commitment to pushing the boundaries of entertainment and technology is evident in everything they do. As a software engineer, I have had the opportunity to work on projects that redefine the future of entertainment. The company culture of creativity and innovation fuels my passion for technology.', 7, 18),
        (TRUE, 90000, 'Hardware Engineer', 'Palo Alto, CA', 'HP Inc. is synonymous with quality and innovation. Working here has been a privilege, and I am proud to contribute to products that empower people and businesses worldwide. The company commitment to excellence drives me to excel in my role every day.', 4, 19),
        (FALSE, 83000, 'Software Engineer', 'Round Rock, TX', 'Dell Technologies is a company driven by innovation and customer satisfaction. As a software engineer, I have had the opportunity to work on projects that solve real-world problems and drive positive change. The company culture of collaboration and diversity fosters creativity and innovation.', 7, 20),
        (TRUE, 94000, 'Software Developer', 'Palo Alto, CA', 'VMware commitment to innovation and excellence is unparalleled. Working here has been a transformative experience, filled with opportunities to learn and grow. The company culture of collaboration and innovation empowers employees to make a meaningful impact.', 8, 21);
        """,
        """
        """,
    ],
]
