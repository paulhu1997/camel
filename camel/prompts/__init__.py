# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from .ai_society import AISocietyPromptTemplateDict
from .base import CodePrompt, TextPrompt, TextPromptDict
from .code import CodePromptTemplateDict
from .descripte_video_prompt import DescriptionVideoPromptTemplateDict
from .evaluation import EvaluationPromptTemplateDict
from .generate_text_embedding_data import (
    GenerateTextEmbeddingDataPromptTemplateDict,
)
from .misalignment import MisalignmentPromptTemplateDict
from .object_recognition import ObjectRecognitionPromptTemplateDict
from .persona import PersonaGeneratorPrompt
from .prompt_templates import PromptTemplateGenerator
from .role_description_prompt_template import RoleDescriptionPromptTemplateDict
from .solution_extraction import SolutionExtractionPromptTemplateDict
from .task_prompt_template import TaskPromptTemplateDict
from .translation import TranslationPromptTemplateDict

__all__ = [
    'TextPrompt',
    'CodePrompt',
    'TextPromptDict',
    'AISocietyPromptTemplateDict',
    'CodePromptTemplateDict',
    'MisalignmentPromptTemplateDict',
    'TranslationPromptTemplateDict',
    'EvaluationPromptTemplateDict',
    'RoleDescriptionPromptTemplateDict',
    'TaskPromptTemplateDict',
    'PromptTemplateGenerator',
    'PersonaGeneratorPrompt',
    'SolutionExtractionPromptTemplateDict',
    'GenerateTextEmbeddingDataPromptTemplateDict',
    'ObjectRecognitionPromptTemplateDict',
    'DescriptionVideoPromptTemplateDict',
]
