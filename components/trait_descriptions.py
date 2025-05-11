def render(st):

    traits = [
        {  
			"name" : "Agreeableness",
			"desc": "The Agreeableness score measures an entrepreneur's willingness to adapt to other people's needs, their ability to forgive and forget, and their propensity to take people as they are, without judgment. If your score for Agreeableness is greater than 4, you are likely to be a team player, cooperative with others, and even-tempered, making you well-suited for more advanced startups that require a group of people to work together to achieve a common goal. If your score is less than 4, you tend to hold grudges, have a propensity to judge others, and stick to your point of view—no matter what, making you well-suited for early-stage startups that require unswerving perseverance to bring a product or service to market."
		},
			
		 { 
			 "name" : "Conscientiousness",
			 "desc": "The Conscientiousness score measures an entrepreneur's inclination to organize their time and their surroundings, their drive to finish what they start, and their propensity to deliberate before they  make decisions. If your score for Conscientiousness is greater than 4, you are likely to be a perfectionist, to keep your spaces well organized, and to think before you act, making you well-suited for more advanced startups that require multiple individuals to deliver their work correctly and on time in order to achieve the  company's goals. If your score is less than 4, you are likely to make decisions based on your impulses, to take a fluid approach to your days, and to focus on the big picture rather than the details, making you well-suited for early-stage startups that require the ability to pivot quickly and intuitively in response to rapidly-changing circumstances."
		 },
			
		{
			"name":"Emotionality",
			"desc":"The Emotionality Score measures an entrepreneur's propensity to anxiety, fear of dangerous situations, and their ability to cope with stress. If your score for Emotionality is greater than 4, you tend to avoid dangerous situations, reach out to others for emotional support, and respond with anxiety to stressful situations, making you well suited for more advanced startups that require strong teamwork combined with higher risk-aversion to manage various stakeholders and a large number of customers. If your score is less than 4, you are not deterred by the prospect of physical danger, get over feelings of anxiety quickly, and tend not to look to others for emotional support in difficult situations, making you well-suited for early-stage startups that face many uncertainties, must cope with a constant stream of stressful situations, and require founders who remain committed to their vision despite the opinions of those around them."
		},
		{
			"name":"Extroversion",
			"desc":"The Extroversion score measures an entrepreneur's inclination to socialize with other people, their confidence in front of groups or crowds, and their energy level. If your score for Extroversion is greater than 4, you are likely to be outgoing, energetic, and to spend your time with colleagues and friends, making you well-suited for more advanced startups that need recognizable leadership in order  to reach their audience (whether customers or funders). This particular strength comes in handy when pitching for funding to your team/customers. If your score is less than 4, you tend to spend your time alone or with a select group of people, prefer to avoid the limelight, and need time on your own to recharge, making you well-suited for early-stage startups that require focused teamwork to build a product or service from scratch in a very short period. "
		},
		{
			"name":"Honesty-Humility",
			"desc":"The Honesty-Humility score measures an entrepreneur's propensity to be direct and transparent with colleagues, how likely they are to stay within the norms, and their interest in the trappings of success. If your score for Honesty-Humility is greater than 4, you are likely to be straightforward, abide by the rules, and won't pretend to be what you're not, making you well-suited for early-stage startups where the odds are against you. If your score is less than 4, you likely tell your colleagues what they want to hear, break rules in order to get ahead, and feel a strong sense of achievement, making you well-suited for more advanced startups that require more pragmatism and diplomacy with stakeholders. "
		},
		{
			"name":"Openness to Experience",
			"desc": "The Openness to Experience score measures an entrepreneur's willingness to take on the new and unexpected,their curiosity about the way things work, and their appreciation of art and nature. If your score for Openness to Experience is greater than 4, you tend to seek intellectual stimulation, enjoy tinkering with things, and ask lots of questions, making you well-suited for early-stage startups that need to approach their work from multiple angles in order to solve unexpected or unforeseen issues. If your score is less than 4, you are likely to get bored at brainstorming sessions, take things as they come, and avoid people/situations that seem radical or unconventional, making you well-suited for more advanced startups that require everyone to perform well-definedtasks effectively in order to successfully deliver on the company’s goals. "
		}
    ]

    for trait in traits:
        with st.expander(trait['name']):
            st.caption(trait['desc'])