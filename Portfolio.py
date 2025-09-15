import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="Ahmed Hamed Attallah - Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for full-width layout and styling
st.markdown("""
    <style>
        .main > div {
            max-width: 100%;
            padding: 0;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Custom styling for full-width sections */
        .full-width {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 40px 0;
        }
        
        .hero-section {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
            padding: 80px 0;
            text-align: center;
        }
        
        .project-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            background: rgba(255, 255, 255, 0.08);
        }
        
        .skills-section {
            background: rgba(0, 0, 0, 0.03);
            padding: 40px 0;
        }
        
        .level-btn {
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            cursor: pointer;
            margin: 5px;
            transition: all 0.3s ease;
        }
        
        .level-btn:hover, .level-btn.active {
            background: linear-gradient(90deg, #4ca1af, #2c5364);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .project-link {
            display: inline-block;
            background: linear-gradient(90deg, #4ca1af, #2c5364);
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            text-align: center;
            margin-top: 15px;
        }
        
        .project-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .project-icon {
            font-size: 2rem;
            margin-bottom: 15px;
            color: #4ca1af;
        }
    </style>
""", unsafe_allow_html=True)

# Portfolio data structure
portfolio_data = {
    "Level 1: Data Fundamentals": [
        {
            "title": "Web Scraping/Data Collection",
            "description": "Python-based Jumia Egypt web scraper. Extracts product details (name, SKU, URL, ratings) and customer reviews from multiple pages. Handles pagination, uses throttling to respect the site, and saves structured data to CSV for ethical data collection.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level1-Task1-webScraping",
            "icon": "🌐"
        },
        {
            "title": "Data Cleaning & Preprocessing",
            "description": "This project transforms raw retail sales data into an analysis-ready asset. It systematically handles missing values (using KNN imputation and deletion), removes outliers, and encodes categorical features. The output is two curated datasets optimized for exploratory analysis and machine learning.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level1-Task2-Data-Cleaning-Preprocessing-",
            "icon": "🧹"
        },
        {
            "title": "Exploratory Data Analysis",
            "description": "This project analyzes supermarket sales data to uncover key trends. Using Python, we found Consumer segment and Technology category drive most revenue, with strong holiday peaks. Insights guide marketing, inventory, and logistics strategies for increased profitability.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level1-Task3-EDA",
            "icon": "📈"
        }
    ],
    "Level 2: Machine Learning": [
        {
            "title": "Predictive Modeling",
            "description": "A machine learning project that predicts house prices using property features. Implemented data preprocessing, feature engineering, and evaluated multiple regression models including Linear Regression, Decision Trees, and Random Forest, with comprehensive performance analysis and visualization of results.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level2-Task1-Predictive-Modeling",
            "icon": "🏠"
        },
        {
            "title": "Classification",
            "description": "A machine learning project classifying iris flowers into three species using Logistic Regression, Random Forest, and SVM. Compares model performance through accuracy metrics, confusion matrices, and ROC curves. SVM achieved the highest accuracy at 96.7%.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level2-Task2-Classification-",
            "icon": "🌷"
        },
        {
            "title": "Clustering",
            "description": "This project applies unsupervised learning (K-Means clustering) to segment customers based on their demographic, behavioral, and transactional characteristics. The goal is to identify distinct customer groups to enable targeted marketing strategies, improve campaign effectiveness, and enhance customer retention.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level2-Task3-Clustring",
            "icon": "👥"
        }
    ],
    "Level 3: Advanced Topics": [
        {
            "title": "Time Series Analysis",
            "description": "Developed ARIMA and SARIMA time series models to forecast YUM stock closing prices. Analyzed historical data, identified trends/seasonality, and built a predictive framework for informed financial decision-making.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level3-Task1-TSA",
            "icon": "📅"
        },
        {
            "title": "Natural Language Processing",
            "description": "NLP project for sentiment analysis and spam detection. Transforms 279 sentiment labels into a binary ham vs. spam classification task. Includes preprocessing, EDA, and a machine learning pipeline with TF-IDF and multiple classifiers, prepared for evaluation and deployment.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level3-Task2-NLP",
            "icon": "📝"
        },
        {
            "title": "Neural Networks",
            "description": "A deep learning project using CNNs on the MNIST dataset, achieving ~98% accuracy with TensorFlow/Keras and hyperparameter tuning. Demonstrates the power of neural networks for image classification tasks.",
            "link": "https://github.com/Ahmed-Hamed-Attallah/CodVeda-Level3-Task3-NN",
            "icon": "🧠"
        }
    ]
}

# Initialize session state for level filtering
if 'current_level' not in st.session_state:
    st.session_state.current_level = "All Levels"

# Hero section
st.markdown("""
    <div class="full-width hero-section">
        <div class="container">
            <h1>Ahmed Hamed Attallah</h1>
            <h3>Data Science Intern at Codveda Technologies</h3>
            <p>Transforming raw data into actionable insights through machine learning and advanced analytics</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Level filter buttons
st.markdown("""
    <div class="container" style="padding: 20px 0; text-align: center;">
        <h2>My Data Science Projects</h2>
        <div style="margin: 20px 0;">
""", unsafe_allow_html=True)

# Create columns for the buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("All Levels", use_container_width=True):
        st.session_state.current_level = "All Levels"

with col2:
    if st.button("Level 1: Fundamentals", use_container_width=True):
        st.session_state.current_level = "Level 1: Data Fundamentals"

with col3:
    if st.button("Level 2: ML", use_container_width=True):
        st.session_state.current_level = "Level 2: Machine Learning"

with col4:
    if st.button("Level 3: Advanced", use_container_width=True):
        st.session_state.current_level = "Level 3: Advanced Topics"

st.markdown("</div></div>", unsafe_allow_html=True)

# Display projects based on selected level
st.markdown("<div class='container'>", unsafe_allow_html=True)

if st.session_state.current_level == "All Levels":
    for level, projects in portfolio_data.items():
        st.markdown(f"<h2>{level}</h2>", unsafe_allow_html=True)
        for project in projects:
            with st.container():
                st.markdown(f"""
                    <div class="project-card">
                        <div class="project-icon">{project['icon']}</div>
                        <h3>{project['title']}</h3>
                        <p>{project['description']}</p>
                        <a href="{project['link']}" target="_blank" class="project-link">View Project</a>
                    </div>
                """, unsafe_allow_html=True)
else:
    st.markdown(f"<h2>{st.session_state.current_level}</h2>", unsafe_allow_html=True)
    for project in portfolio_data[st.session_state.current_level]:
        with st.container():
            st.markdown(f"""
                <div class="project-card">
                    <div class="project-icon">{project['icon']}</div>
                    <h3>{project['title']}</h3>
                    <p>{project['description']}</p>
                    <a href="{project['link']}" target="_blank" class="project-link">View Project</a>
                </div>
            """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Skills section
st.markdown("""
    <div class="full-width skills-section">
        <div class="container">
            <h2 style="text-align: center;">Technical Skills</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px;">
                <div>
                    <h3>Data Manipulation & Analysis</h3>
                    <ul>
                        <li>Python (Pandas, NumPy)</li>
                        <li>Data Cleaning & Preprocessing</li>
                        <li>Web Scraping</li>
                        <li>Exploratory Data Analysis</li>
                    </ul>
                </div>
                <div>
                    <h3>Machine Learning</h3>
                    <ul>
                        <li>Regression Models</li>
                        <li>Classification Algorithms</li>
                        <li>Clustering Techniques</li>
                        <li>Model Evaluation</li>
                    </ul>
                </div>
                <div>
                    <h3>Advanced Techniques</h3>
                    <ul>
                        <li>Time Series Analysis</li>
                        <li>Natural Language Processing</li>
                        <li>Neural Networks & Deep Learning</li>
                        <li>Data Visualization</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="container" style="text-align: center; padding: 40px 0;">
        <p>Ahmed Hamed Attallah - Data Science Portfolio</p>
        <p>© 2023 | Created during Data Science Internship at Codveda Technologies</p>
    </div>
""", unsafe_allow_html=True)
