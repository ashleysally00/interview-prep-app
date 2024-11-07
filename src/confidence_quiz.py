# src/confidence_quiz.py

class ConfidenceQuiz:
    def __init__(self):
        self.questions = [
            {
                "id": 1,
                "question": "In a team meeting, you strongly disagree with a colleague's approach. What do you typically do?",
                "options": {
                    "A": "Wait until after the meeting to discuss it privately with your colleague",
                    "B": "Raise your concerns during the meeting, presenting your alternative with supporting data",
                    "C": "Keep your opinion to yourself to avoid potential conflict"
                },
                "scores": {
                    "A": 2,  # Diplomatic but not fully confident
                    "B": 3,  # Confident and professional
                    "C": 1   # Lack of confidence
                }
            },
            {
                "id": 2,
                "question": "Your manager asks if anyone wants to lead an important new project. What's your response?",
                "options": {
                    "A": "Immediately volunteer, highlighting your relevant skills",
                    "B": "Wait to see if anyone else volunteers first",
                    "C": "Consider volunteering but worry about potential failure"
                },
                "scores": {
                    "A": 3,  # High confidence
                    "B": 2,  # Moderate confidence
                    "C": 1   # Low confidence
                }
            },
            {
                "id": 3,
                "question": "You've achieved a significant milestone in your project. How do you handle it?",
                "options": {
                    "A": "Briefly mention it in your status report",
                    "B": "Share the achievement and credit your team's contributions",
                    "C": "Wait for others to notice and mention it"
                },
                "scores": {
                    "A": 2,
                    "B": 3,
                    "C": 1
                }
            },
            {
                "id": 4,
                "question": "During salary negotiations, what's your typical approach?",
                "options": {
                    "A": "Accept the initial offer to avoid seeming demanding",
                    "B": "Research market rates and negotiate based on your value",
                    "C": "Feel uncomfortable but ask for a small increase"
                },
                "scores": {
                    "A": 1,
                    "B": 3,
                    "C": 2
                }
            },
            {
                "id": 5,
                "question": "When facing a challenging task outside your comfort zone, you usually:",
                "options": {
                    "A": "Take it on as a growth opportunity, seeking help when needed",
                    "B": "Feel anxious but try your best to complete it",
                    "C": "Try to pass it to someone more experienced"
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            }
        ]
        
    def calculate_score(self, answers):
        """Calculate total score and return feedback."""
        total_score = sum(self.questions[i]["scores"][answer] for i, answer in enumerate(answers))
        max_possible = len(self.questions) * 3
        score_percentage = (total_score / max_possible) * 100
        
        if score_percentage >= 80:
            confidence_level = "High Confidence"
            feedback = self._get_high_confidence_feedback()
        elif score_percentage >= 60:
            confidence_level = "Moderate Confidence"
            feedback = self._get_moderate_confidence_feedback()
        else:
            confidence_level = "Developing Confidence"
            feedback = self._get_developing_confidence_feedback()
        
        return {
            "score": total_score,
            "max_score": max_possible,
            "percentage": score_percentage,
            "feedback": feedback
        }
    
    def _get_high_confidence_feedback(self):
        return {
            "level": "High Confidence",
            "summary": "You exhibit strong workplace confidence!",
            "strengths": [
                "Comfortable taking initiative",
                "Effective at self-advocacy",
                "Strong leadership potential"
            ],
            "next_steps": [
                "Consider mentoring others to build their confidence",
                "Take on stretch assignments to further grow",
                "Share your experiences in professional forums"
            ],
            "interview_tips": [
                "Use specific examples of leadership in interviews",
                "Highlight instances where your confidence led to success",
                "Express interest in growth opportunities"
            ]
        }
    
    def _get_moderate_confidence_feedback(self):
        return {
            "level": "Moderate Confidence",
            "summary": "You have a good foundation of confidence with room to grow.",
            "strengths": [
                "Capable of speaking up when necessary",
                "Willing to take on challenges",
                "Shows potential for leadership"
            ],
            "next_steps": [
                "Practice voicing your opinions more in meetings",
                "Take on more visible projects",
                "Set specific goals for professional growth"
            ],
            "interview_tips": [
                "Prepare examples of overcoming challenges",
                "Practice discussing achievements comfortably",
                "Focus on growth mindset in responses"
            ]
        }
    
    def _get_developing_confidence_feedback(self):
        return {
            "level": "Developing Confidence",
            "summary": "You have opportunities to build your workplace confidence.",
            "strengths": [
                "Thoughtful in approach to work",
                "Careful consideration of options",
                "Potential for growth"
            ],
            "next_steps": [
                "Start with small wins to build confidence",
                "Find a mentor for guidance and support",
                "Practice self-advocacy in low-stakes situations"
            ],
            "interview_tips": [
                "Focus on learning experiences and growth",
                "Prepare thoroughly to boost confidence",
                "Practice interview responses with trusted friends"
            ]
        }