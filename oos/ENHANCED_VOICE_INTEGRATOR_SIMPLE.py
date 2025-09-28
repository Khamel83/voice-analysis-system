#!/usr/bin/env python3
"""
Enhanced Voice Integrator - Simplified Version
Integrates enhanced content analysis with existing voice generation system
"""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class EnhancedVoiceIntegrator:
    """Integrates enhanced analysis with voice generation"""

    def __init__(self):
        self.analysis_db = "/Users/khamel83/dev/Speech/data/enhanced_analysis.db"
        self.enhanced_prompt_path = "/Users/khamel83/dev/Speech/prompts/ENHANCED_VOICE_PROFILE.txt"

        # Load enhanced prompt
        try:
            with open(self.enhanced_prompt_path, 'r') as f:
                self.enhanced_prompt = f.read()
        except:
            self.enhanced_prompt = ""

    def integrate_system(self) -> Dict:
        """Complete integration process"""
        print("🔗 INTEGRATING ENHANCED SYSTEM")
        print("=" * 50)

        integration = {
            'load_analysis': self._load_enhanced_analysis(),
            'update_voice_generator': self._update_voice_generator(),
            'generate_final_profile': self._generate_final_4k_profile(),
        }

        self._save_integration_report(integration)

        return integration

    def _load_enhanced_analysis(self) -> Dict:
        """Load enhanced analysis from database"""
        print("📂 Loading enhanced analysis...")

        try:
            conn = sqlite3.connect(self.analysis_db)
            cursor = conn.cursor()

            cursor.execute('SELECT analysis_json FROM enhanced_analysis ORDER BY analysis_date DESC LIMIT 1')
            result = cursor.fetchone()

            if result:
                analysis = json.loads(result[0])
                print(f"   Loaded analysis with {len(analysis)} sections")
                conn.close()
                return analysis
            else:
                print("   No analysis found in database")
                conn.close()
                return {}

        except Exception as e:
            print(f"   Error loading analysis: {e}")
            return {}

    def _update_voice_generator(self) -> Dict:
        """Update AI voice generator with enhanced prompts"""
        print("🤖 Creating enhanced voice generator...")

        if not self.enhanced_prompt:
            print("   Warning: Enhanced prompt not found")
            return {'status': 'failed', 'reason': 'enhanced_prompt_missing'}

        # Create enhanced generator that uses the new prompt
        enhanced_generator_code = self._create_enhanced_generator_code()

        # Save enhanced generator
        generator_path = "/Users/khamel83/dev/Speech/src/enhanced_ai_voice_generator.py"
        with open(generator_path, 'w') as f:
            f.write(enhanced_generator_code)

        print(f"   Enhanced generator saved: {generator_path}")
        return {'status': 'success', 'generator_path': generator_path}

    def _create_enhanced_generator_code(self) -> str:
        """Create the enhanced generator code without f-string issues"""
        # Create the template with proper string formatting
        template = '''#!/usr/bin/env python3
"""
Enhanced AI Voice Generator
Uses enhanced content analysis for realistic voice generation
"""

import requests
import random
from typing import List, Dict
from pathlib import Path
import json

class EnhancedAIVoiceGenerator:
    """AI Voice Generator with enhanced content knowledge"""

    def __init__(self):
        self.enhanced_prompt = """{ENHANCED_PROMPT}"""
        self.api_key = self._load_api_key()
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "google/gemini-2.5-flash-lite"

    def _load_api_key(self) -> str:
        """Load API key from environment or config"""
        import os
        api_key = os.getenv('OPENROUTER_API_KEY', '')
        if api_key:
            return api_key

        try:
            config_path = Path('/Users/khamel83/dev/Speech/config/api_keys.json')
            if config_path.exists():
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    return config.get('openrouter_api_key', '')
        except:
            pass

        return ''

    def generate_enhanced_content(self, theme: str, target_length: int = 250) -> str:
        """Generate content using enhanced voice profile"""

        if not self.api_key:
            return self._fallback_generation(theme, target_length)

        # Create prompt that includes knowledge boundaries
        prompt = f"""{{self.enhanced_prompt}}

TASK: Generate content on theme '{theme}' that matches the voice profile above.
LENGTH: Approximately {{target_length}} characters
REQUIREMENTS:
- Stay within knowledge boundaries (avoid alcohol, sports, religion)
- Match Omar's direct, purposeful communication style
- Include specific details and practical information
- Adapt formality based on theme context

Generate now:\"\"\"

        try:
            headers = {{
                "Authorization": f"Bearer {{self.api_key}}",
                "Content-Type": "application/json"
            }}

            payload = {{
                "model": self.model,
                "messages": [{{"role": "user", "content": prompt}}],
                "max_tokens": max(100, target_length // 3),
                "temperature": 0.8
            }}

            response = requests.post(self.base_url, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                result = response.json()
                generated_text = result['choices'][0]['message']['content'].strip()
                print(f"✅ Enhanced generation: {{len(generated_text)}} chars")
                return generated_text
            else:
                print(f"❌ API error: {{response.status_code}}")
                return self._fallback_generation(theme, target_length)

        except Exception as e:
            print(f"❌ Generation failed: {{e}}")
            return self._fallback_generation(theme, target_length)

    def _fallback_generation(self, theme: str, target_length: int) -> str:
        """Enhanced fallback using knowledge boundaries"""
        # Use themes and content that match known domains
        theme_templates = {{
            'work': "hey regarding the project, we need to figure out the next steps. let me know when you're free to discuss.",
            'planning': "so for the weekend plans, i'm thinking we should meet around 2pm. does that work for everyone?",
            'academic': "for the assignment, we need to focus on the main requirements. have you started the outline yet?",
            'social': "hey, wanna grab coffee sometime next week? i'm thinking tuesday or wednesday afternoon."
        }}

        base = theme_templates.get(theme, theme_templates['social'])
        while len(base) < target_length * 0.8:
            base += " let me know what works for you."

        return base[:target_length]

if __name__ == "__main__":
    generator = EnhancedAIVoiceGenerator()
    result = generator.generate_enhanced_content("work", 200)
    print(f"Generated: {{result}}")
'''

        # Replace the placeholder with the actual enhanced prompt
        enhanced_prompt_escaped = self.enhanced_prompt.replace('"""', '\\"\\"\\"')
        return template.replace('{ENHANCED_PROMPT}', enhanced_prompt_escaped)

    def _generate_final_4k_profile(self) -> Dict:
        """Generate the final 4,000-token enhanced voice profile"""
        print("📄 Generating final 4K voice profile...")

        # Load enhanced analysis
        enhanced_analysis = self._load_enhanced_analysis()

        # Build comprehensive final profile
        final_profile = {
            'profile_metadata': {
                'version': 'enhanced_2.0',
                'created': datetime.now().isoformat(),
                'corpus_size': enhanced_analysis.get('corpus_stats', {}).get('total_chars', 0),
                'analysis_method': 'embedding_clustering + vocabulary_analysis'
            },
            'content_domains': self._extract_content_domains(enhanced_analysis),
            'writing_patterns': self._extract_writing_patterns(enhanced_analysis),
            'knowledge_boundaries': self._extract_knowledge_boundaries(enhanced_analysis),
            'vocabulary_domains': self._extract_vocabulary_domains(enhanced_analysis),
            'authentic_examples': self._extract_authentic_examples(enhanced_analysis),
            'generation_guidelines': self._create_generation_guidelines(enhanced_analysis)
        }

        # Save final profile
        final_profile_path = "/Users/khamel83/dev/Speech/prompts/FINAL_ENHANCED_VOICE_PROFILE_4K.json"
        with open(final_profile_path, 'w') as f:
            json.dump(final_profile, f, indent=2)

        print(f"   Final 4K profile saved: {final_profile_path}")
        return {'status': 'success', 'profile_path': final_profile_path}

    # Helper methods for final profile generation
    def _extract_content_domains(self, analysis: Dict) -> Dict:
        return {
            'academic_writing': analysis.get('vocabulary_analysis', {}).get('by_content_type', {}).get('academic', {}),
            'professional_communication': analysis.get('vocabulary_analysis', {}).get('by_content_type', {}).get('work', {}),
            'personal_coordination': analysis.get('vocabulary_analysis', {}).get('by_content_type', {}).get('social', {}),
            'technical_problem_solving': analysis.get('vocabulary_analysis', {}).get('technical_domains', [])
        }

    def _extract_writing_patterns(self, analysis: Dict) -> Dict:
        return analysis.get('style_patterns', {})

    def _extract_knowledge_boundaries(self, analysis: Dict) -> Dict:
        return analysis.get('knowledge_boundaries', {})

    def _extract_vocabulary_domains(self, analysis: Dict) -> Dict:
        return analysis.get('vocabulary_analysis', {})

    def _extract_authentic_examples(self, analysis: Dict) -> List[str]:
        return [
            "hey can you ask mom if she can get a hp648c color cartridge from work. If she can that would be really good, ok thanks",
            "Dudes, I'm coming into Chicago Friday the 26th and then sticking around to attend a conference on Monday and Tuesday",
            "with sam. im not sure what you told him (its not important anymore) but it seems as though my explanation was 'possibly the most obnoxious email ive ever received'"
        ]

    def _create_generation_guidelines(self, analysis: Dict) -> Dict:
        return {
            'formality_adaptation': 'Adapt formality based on context',
            'knowledge_constraints': 'Stay within identified knowledge boundaries',
            'communication_style': 'Direct, purposeful, minimal filler',
            'content_specificity': 'Include specific details and practical information'
        }

    def _save_integration_report(self, integration: Dict):
        """Save integration report"""
        report_path = "/Users/khamel83/dev/Speech/oos/INTEGRATION_REPORT.json"
        with open(report_path, 'w') as f:
            json.dump(integration, f, indent=2, default=str)

        print(f"💾 Integration report saved: {report_path}")

if __name__ == "__main__":
    integrator = EnhancedVoiceIntegrator()
    integration = integrator.integrate_system()

    print("\n🎯 INTEGRATION COMPLETE")
    print("=" * 50)
    print(f"Analysis loaded: {integration.get('load_analysis', {}).get('corpus_stats', {}).get('total_chars', 0)} chars analyzed")
    print(f"Generator updated: {integration.get('update_voice_generator', {}).get('status', 'unknown')}")
    print(f"Final profile: {integration.get('generate_final_profile', {}).get('status', 'unknown')}")
