import os
from datetime import datetime
import random
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=openai_api_key)


# Simulated campaign data - in a real implementation, this would come from an API
CAMPAIGN_DATA = {
    "email_campaign_q1": {
        "open_rate": 22.5,
        "click_rate": 3.8,
        "conversion_rate": 1.2,
        "total_sends": 15000,
        "top_performing_subject": "Transform your marketing with AI tools",
        "worst_performing_subject": "Newsletter: Marketing Updates for Q1",
        "peak_engagement_day": "Tuesday",
        "peak_engagement_time": "10:00 AM",
        "audience_segments": ["Marketing Managers", "Digital Marketers", "CMOs"],
        "content_themes": ["AI Marketing", "Marketing Automation", "ROI Optimization"]
    },
    "social_campaign_summer": {
        "engagement_rate": 4.2,
        "click_through_rate": 2.1,
        "conversion_rate": 0.8,
        "total_impressions": 85000,
        "top_performing_platform": "LinkedIn",
        "worst_performing_platform": "Twitter",
        "top_performing_content": "Case study: How Company X increased leads by 300%",
        "audience_demographics": {"25-34": 40, "35-44": 35, "45-54": 20, "55+": 5},
        "hashtags": ["#MarketingTips", "#AIMarketing", "#LeadGeneration"]
    },
    "webinar_series_2023": {
        "registration_rate": 8.3,
        "attendance_rate": 65.2,
        "conversion_rate": 12.5,
        "attendee_count": 520,
        "average_watch_time": "42 minutes",
        "top_question_themes": ["Implementation", "Integration", "Pricing"],
        "satisfaction_score": 4.7,
        "repeat_attendees": 28,
        "content_topics": ["AI Strategy", "Content Automation", "Marketing ROI"]
    }
}


def analyze_campaign_data(campaign_id):
    """
    Analyze the performance of a marketing campaign

    Args:
        campaign_id (str): ID of the campaign to analyze

    Returns:
        dict: Campaign analysis with key metrics and insights
    """
    if campaign_id not in CAMPAIGN_DATA:
        return {
            "error": f"Campaign '{campaign_id}' not found",
            "available_campaigns": list(CAMPAIGN_DATA.keys())
        }

    campaign = CAMPAIGN_DATA[campaign_id]

    # Simulate analysis of the data
    insights = []
    recommendations = []

    # Generate insights based on campaign type
    if "open_rate" in campaign:  # Email campaign
        if campaign["open_rate"] > 20:
            insights.append("Open rate is above industry average (20%)")
        else:
            insights.append("Open rate is below industry average (20%)")
            recommendations.append("Improve subject lines and sender name")

        if campaign["click_rate"] < 4:
            insights.append("Click rate could be improved")
            recommendations.append("Review call-to-action clarity and placement")

    elif "engagement_rate" in campaign:  # Social campaign
        if campaign["engagement_rate"] > 3:
            insights.append(f"Strong engagement rate on {campaign['top_performing_platform']}")
        else:
            insights.append("Engagement rate needs improvement")
            recommendations.append("Increase visual content and post at optimal times")

    elif "attendance_rate" in campaign:  # Webinar campaign
        if campaign["attendance_rate"] > 60:
            insights.append("Excellent attendance rate")
        else:
            insights.append("Attendance rate could be improved")
            recommendations.append("Send more reminder emails and add calendar invites")

    # Common recommendations
    if campaign.get("conversion_rate", 0) < 2:
        insights.append("Conversion rate needs improvement")
        recommendations.append("Strengthen calls-to-action and landing page design")

    analysis = {
        "campaign_id": campaign_id,
        "metrics": campaign,
        "insights": insights,
        "recommendations": recommendations,
        "analysis_date": datetime.now().strftime("%Y-%m-%d")
    }

    return analysis


def generate_content(topic, audience, tone="professional", platform=None, length="medium"):
    """
    Generate high-quality marketing content using enhanced templates

    Args:
        topic (str): The main topic/theme of the content
        audience (str): Target audience
        tone (str): Tone of voice (professional, casual, enthusiastic)
        platform (str): Social platform or content destination
        length (str): Content length (short, medium, long)

    Returns:
        dict: Generated content with metadata
    """
    from datetime import datetime
    import random

    # Initialize response structure
    response = {
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "platform": platform,
        "length": length,
        "content": "",
        "hashtags": [],
        "estimated_reading_time": "",
        "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # Enhanced templates for professional tone
    professional_templates = [
        "New research reveals that {topic} is transforming how {audience} approach strategic decisions. Organizations implementing these advanced solutions are seeing up to 40% higher engagement and 25% improved ROI. Learn the key implementation frameworks that industry leaders are using to maintain competitive advantage.",
        
        "In today's data-driven marketplace, {audience} need to leverage {topic} to stay ahead. Our analysis of 500+ industry leaders shows that early adopters are experiencing 3X faster optimization and significantly higher conversion rates. Here's the strategic roadmap for implementation that's generating measurable results.",
        
        "The convergence of {topic} with traditional frameworks presents unprecedented opportunities for {audience}. Forward-thinking organizations are reducing development cycles by 60% while improving precision metrics. Discover the implementation pathway that leading companies are following for sustainable growth."
    ]

    # Enhanced templates for casual tone
    casual_templates = [
        "Have you been wondering how {topic} could transform your results? We've been testing these approaches with clients across industries, and the outcomes are honestly impressive. One client saw their engagement metrics double in just 6 weeks! Here's what we're learning that you can apply right away...",
        
        "Let's talk about {topic} - it's completely reshaping possibilities for {audience} everywhere. We've collected insights from dozens of successful implementations, and there's a clear pattern emerging among top performers. The best part? The implementation pathway is more accessible than most realize!",
        
        "The {topic} revolution isn't coming—it's already here, and {audience} who are jumping in now are seeing fantastic outcomes. We've been tracking early adopters, and they're reporting an average 45% improvement in effectiveness. Here's your roadmap to joining their ranks."
    ]

    # Enhanced templates for enthusiastic tone
    enthusiastic_templates = [
        "🚀 BREAKTHROUGH ALERT! {topic} is absolutely TRANSFORMING how {audience} connect with their market! Latest research shows a STAGGERING 87% improvement in key metrics when properly implemented! Don't miss this opportunity to revolutionize your approach!",
        
        "🔥 GAME-CHANGER for {audience}! {topic} is redefining what's possible in today's landscape! Organizations implementing these approaches are seeing INCREDIBLE results—some reporting 3X HIGHER conversion rates! Here's how YOU can harness this power! 🔥",
        
        "⚡ ATTENTION {audience}! The {topic} revolution is creating MASSIVE opportunities that most are missing! Exclusive analysis shows early adopters outperforming competitors by 155%! Don't get left behind—these insights will TRANSFORM your strategy! ⚡"
    ]

    # Select appropriate template based on tone
    if tone.lower() in ["professional", "formal", "insightful", "informative", "educational"]:
        templates = professional_templates
    elif tone.lower() in ["casual", "conversational", "friendly", "approachable"]:
        templates = casual_templates
    elif tone.lower() in ["enthusiastic", "exciting", "energetic", "persuasive", "engaging"]:
        templates = enthusiastic_templates
    else:
        templates = professional_templates

    # Select a random template from the appropriate category
    template = random.choice(templates)

    # Generate content by filling in the template
    content = template.format(topic=topic, audience=audience)

    # Adjust content length
    if length.lower() == "short":
        # For short content, use just the first sentence
        first_sentence_end = content.find('.')
        if first_sentence_end > 0:
            content = content[:first_sentence_end + 1]
    elif length.lower() == "long":
        # For long content, add additional context
        additional_context = f"\n\nOur team has analyzed the latest trends in {topic} and compiled actionable strategies specifically designed for {audience}. The data reveals that companies implementing these approaches are consistently outperforming market averages across key metrics. By adopting these evidence-based methodologies, you can position your organization at the forefront of industry developments while optimizing resource allocation and maximizing return on investment."
        content += additional_context

    # Generate platform-specific elements
    if platform:
        if platform.lower() == "linkedin":
            response["hashtags"] = [
                f"#{topic.replace(' ', '').replace(':', '')}",  # Remove spaces and colons from hashtag
                "#CFO",
                "#AIinFinance",
                "#FinancialLeadership",
                "#DigitalTransformation",
                "#FinanceInnovation"
            ]
            # Refined content for CFOs on LinkedIn
            if length.lower() == "medium":
                content = f"CFOs are increasingly leveraging AI to drive strategic financial decisions. From automating routine tasks to providing predictive insights, AI empowers CFOs to optimize resource allocation, mitigate risks, and enhance overall financial performance. #CFO #AIinFinance #FinanceTransformation"
            elif length.lower() == "long":
                content = f"CFOs are at the forefront of digital transformation, with AI emerging as a crucial tool for strategic financial management. By automating routine tasks, AI frees up CFOs to focus on higher-level analysis and decision-making.  Predictive analytics, powered by AI, enable CFOs to forecast financial performance with greater accuracy, identify potential risks, and optimize resource allocation.  Moreover, AI facilitates enhanced data visualization, providing CFOs with clear, actionable insights to drive growth and profitability. #CFO #AIinFinance #FinanceTransformation #DigitalTransformation #FinancialLeadership"
            else:
                 content = f"AI is changing the role of the CFO.  Here's how #CFOs can use it. #AIinFinance"

            response["estimated_reading_time"] = "1-2 min read"
            # Debugging LinkedIn content
            print(f"DEBUG: LinkedIn content before return: {content}")
        elif platform.lower() in ["twitter", "x"]:
            # Ensure content is concise for Twitter
            if len(content) > 280:
                content = content[:277] + "..."
            response["hashtags"] = [
                f"#{topic.replace(' ', '')}",
                "#MarketingStrategy"
            ]

        elif platform.lower() == "instagram":
            response["hashtags"] = [
                f"#{topic.replace(' ', '')}",
                "#MarketingTips",
                "#BusinessStrategy",
                "#DigitalMarketing",
                "#GrowthHacking"
            ]

        elif platform.lower() == "email":
            # Add email-specific formatting
            subject_line = f"New insights on {topic} for {audience}"
            content = f"Subject: {subject_line}\n\nHello {audience} professional,\n\n{content}\n\nBest regards,\nYour Marketing Team"

    # Update response with generated content
    response["content"] = content
    print(f"DEBUG: generate_content output: {response}")  # <-- ADDED THIS LINE
    return response



def schedule_content(content, platform, publish_date, time_slot=None):
    """
    Schedule content for publishing on specified platform

    Args:
        content (str): The content to be scheduled
        platform (str): Platform to publish on
        publish_date (str): Date to publish (YYYY-MM-DD)
        time_slot (str): Optional time slot (e.g., "9:00 AM")

    Returns:
        dict: Scheduling confirmation with details
    """
    # Validate date format
    try:
        parsed_date = datetime.strptime(publish_date, "%Y-%m-%d")
        # Ensure date is not in the past
        if parsed_date < datetime.now():
            return {"error": "Cannot schedule content in the past"}
    except ValueError:
        return {"error": "Invalid date format. Use %Y-%m-%d"}

    # Set default time slot based on platform best practices if not provided
    if not time_slot:
        if platform.lower() == "linkedin":
            time_slot = "9:00 AM"
        elif platform.lower() == "twitter" or platform.lower() == "x":
            time_slot = "12:00 PM"
        elif platform.lower() == "instagram":
            time_slot = "6:00 PM"
        elif platform.lower() == "email":
            time_slot = "10:00 AM"
        else:
            time_slot = "9:00 AM"

    # Content validation based on platform
    warnings = []
    if platform.lower() == "twitter" or platform.lower() == "x":
        if len(content) > 280:
            warnings.append("Content exceeds Twitter's 280 character limit. It will be truncated.")
            content = content[:277] + "..."

    # In a real implementation, this would integrate with a scheduling API
    # For demo purposes, we'll return a confirmation

    response = {
        "status": "scheduled",
        "platform": platform,
        "publish_date": publish_date,
        "time_slot": time_slot,
        "content_preview": content[:100] + "..." if len(content) > 100 else content,
        "full_content_length": len(content),
        "warnings": warnings,
        "scheduling_id": f"sched_{int(datetime.now().timestamp())}",
        "scheduled_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return response


import os
from dotenv import load_dotenv
from openai import OpenAI  # Corrected import
import json

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=openai_api_key)  # Initialize client

# Define the system prompt
workflow_system_prompt = """
You are a marketing workflow agent. Your job is to help users automate their marketing tasks.
You can analyze campaign data, generate content, and schedule posts.
"""

# Define the function to extract JSON
def extract_json(text):
    """
    Extracts the first JSON object from a given text string.

    Args:
        text (str): The text string to search for JSON within.

    Returns:
        list: A list containing the extracted JSON object (as a dict), or an empty list if no JSON is found.
    """
    json_start = text.find('{')
    if json_start == -1:
        return []
    json_end = text.find('}', json_start) + 1
    if json_end == 0:
        return []

    json_str = text[json_start:json_end]
    try:
        json_object = json.loads(json_str)
        return [json_object]  # Wrap in a list for consistency
    except json.JSONDecodeError:
        return []



# Available actions
available_actions = {
    "analyze_campaign_data": analyze_campaign_data,
    "generate_content": generate_content,
    "schedule_content": schedule_content
}


def generate_response(messages, model="gpt-3.5-turbo"):
    """Generate a response from the language model"""
    try:
        response = client.chat.completions.create(  # corrected function
            model=model,
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {e}"


def run_workflow_agent():
    """Run the Marketing Workflow Agent"""
    print("\n=== Marketing Workflow Agent ===")
    print("This agent can analyze campaigns, generate content, and schedule posts.")
    print("Type 'exit' to quit.\n")

    # Initialize conversation with system prompt
    messages = [{"role": "system", "content": workflow_system_prompt}]

    while True:
        # Get user input
        user_input = input("\nWhat marketing task can I help you with? ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Add user input to messages
        messages.append({"role": "user", "content": user_input})

        # Initialize loop variables
        turn_count = 1
        max_turns = 5

        # Agent loop
        while turn_count < max_turns:
            print(f"\n[Thinking... Step {turn_count}/{max_turns}]")

            # Get response from language model
            ai_response = generate_response(messages)
            print(f"\nWorkflow Agent: {ai_response}")

            # Check if we need to execute an action
            json_function = extract_json(ai_response)

            if json_function:
                # We found a function call
                function_name = json_function[0]['function_name']
                function_parms = json_function[0]['function_parms']

                # Check if function exists
                if function_name not in available_actions:
                    print(f"Error: Unknown action '{function_name}'")
                    break

                # Execute the function
                print(f"\n[Executing {function_name}...] ")  # add action name
                action_function = available_actions[function_name]
                result = action_function(**function_parms)

                # Format the result
                function_result_message = f"Action_Response: {result}"
                print(f"\n[Result: {function_result_message}]")  # print result

                # Add messages to conversation
                messages.append({"role": "assistant", "content": ai_response})
                messages.append({"role": "user", "content": function_result_message})

                turn_count += 1
            else:
                # No function call, we're done
                messages.append({"role": "assistant", "content": ai_response})
                break
        
        # Print the final output from the agent
        print(messages[-1]['content'])
if __name__ == "__main__":
    run_workflow_agent()
