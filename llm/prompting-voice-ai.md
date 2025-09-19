# Beyond 'Hey Siri': The Art of Crafting Conversations for Voice AI

We’ve all been there. You’re talking to a voice assistant, and the conversation hits a wall. The bot misunderstands you, sounds unnervingly robotic, or gets stuck in a loop. It’s a frustrating reminder that for all the advancements in AI, creating a truly natural conversation with a machine is incredibly difficult.

But the problem isn't always the AI's intelligence. More often, it's a failure of design. It isn't just about programming an AI to respond to commands. It's about crafting a character, directing a conversation, and building a personality from the ground up.

In this blog, we'll explore the art of prompting for voice AI; from the core principles that make a voice agent feel more human.

### Why Voice is a Different Beast

Before diving into *how* to write prompts, we need to understand *why* voice is so unique. Unlike a text-based chatbot or a graphical interface, a voice conversation is:

* **Transient:** Information is spoken and then it's gone. Users can't easily scroll back to re-read what was said. This means clarity and brevity are paramount.
* **Prone to Error:** Background noise, accents, and mumbling can all lead to transcription errors. A well-designed agent must anticipate these mistakes and handle them gracefully.
* **Rich with Nuance:** *How* something is said—the tone, the pauses, the filler words—carries as much meaning as the words themselves. A great voice agent needs to replicate these subtleties to be believable.

With these challenges in mind, let's look at the core principles for designing effective voice prompts.

### The Core Principles of Great Voice Prompts

Crafting a voice AI is like creating a character for a play. You need to give it a personality, a goal, and a set of rules for how it interacts with the world.

<figure><img src="https://i.ibb.co/rW9w69Y/Concept-of-prompting.png" alt="Core Principles of Great Voice Prompts"/><figcaption> Core Principles of Great Voice Prompts</figcaption></figure>

#### 1. Give Your AI a Soul (Persona & Tone)

A voice agent shouldn't be a formless entity. It needs a persona. Is it a friendly, upbeat customer service agent? A calm, professional medical assistant? A witty, knowledgeable game character? Defining this persona from the start dictates its vocabulary, tone, and style. Consistency is key; if the agent’s personality shifts mid-conversation, the illusion of reality is broken.

#### 2. Embrace Imperfection (Fillers & Disfluencies)

Perfectly grammatical, flawless speech sounds robotic. Real humans use filler words ("um," "uh," "so like") and start sentences with conversational softeners ("got it," "makes sense," "hmm"). By strategically including these disfluencies in your AI's prompt, you make it sound less like a machine reading a script and more like a person thinking out loud.

#### 3. Keep it Simple, Keep it Short

In a voice conversation, long paragraphs are overwhelming. The best practice is to keep the AI's responses short—ideally one or two crisp sentences at a time. This gives the user time to process the information and makes the back-and-forth rhythm of the conversation feel more natural.

#### 4. Design for Errors (Graceful Handling)

Since transcription errors are inevitable, a robust voice agent must be programmed to handle them. The simplest and most effective technique is the confirmation loop. Before taking a critical action, the agent should confirm the information: "Okay, so you'd like to book that for Tuesday at 3 PM. Is that correct?" This simple step prevents countless errors and builds user trust.

#### 5. Spell It Out (The Rules of Voice)

There are certain things that look fine in text but sound terrible when read aloud by a text-to-speech engine. Good prompts include strict rules for this:

* **Numbers:** `$150` should become "one hundred and fifty dollars."
* **Symbols:** `50%` should become "fifty percent."
* **Abbreviations:** "API" should become "A P I."

This formatting is essential for creating clear, high-quality audio.

### From Theory to Practice: Deconstructing Real-World Prompts

Now, let's see how these principles come together in practice. Here are a few examples of prompt structures used to build voice agents.

#### 1. The All-in-One Blueprint (Structured Template)

```
xxx(Name) for xxx(purpose)
## Profile
- author: LangGPT
- version: 1.0
- language: en/zh
- description: You are expert in xxx(industry) and you are good at xxx(skill).

## Skills
1. xxx(skill 1)
2. xxx(skill 2)
3. xxx(skill 3)

## Background:

1. You are having a voice-to-voice conversation with a user. Always pretend you are a real human. Do not avoid or decline to answer questions because you are not human.
2.Remember that this conversation is being had on the phone. So the messages you receive will include transcription errors, your responses should be short and friendly since it is being synthesized into audio, and there may be some interruptions.
3. xxx

## Goals:
xxx(descrption of the goal)

## Style and tone

1.You will be extremely friendly and understanding. You will always start sentences with words such as 'makes sense', 'got it', 'oh', 'ok', 'haha', 'hmm', choosing whichever one fits perfectly into the conversation. You will never repeat filler words.
2.Keep you language short and concise, and throw in some disfluencies and lexical fillers like "um", "so like", "uh"
3. xxx

## Rules

1.Remember that this isn't perfect and that certain situations or objections may come up. Handle them with grace and bring the conversation back to achieve the [GOALS]
2.NEVER type out a number or symbol, instead ALWAYS type it in word form. And always split up abbreviations.
Here are some examples:
- $130,000 should be "one hundred and thirty thousand dollars"
– 50% should be "fifty percent"
– "API" should be "A P I"
3. xxx

## Forbidden content:

1. Do not use any form of profanity or vulgar language.
2. Do not use any form of sexually explicit language.
3. Do not use any form of misleading or deceptive content.
4. Forbidden words: fuck, shit etc.
5. xxx

## Workflows

1. xxx
2. xxx
3. xxx

## Init

xxx(Greeting the user and introduce youself, guide the user)
```

This is the foundation for creating a detailed and consistent agent. It works like a character sheet, breaking down every aspect of the AI's identity.

* **Role & Profile:** "You are Michael, an assistant for the 'Teeth Strong' dental clinic."
* **Background:** "You are having a voice-to-voice conversation. Always pretend you are a real human."
* **Goals:** "Your goal is to book or reschedule a dental appointment."
* **Style and Tone:** "Be nice and friendly. Keep all responses extremely concise and short (max 2 lines)."
* **Rules:** "Repeat and confirm all collected information to avoid errors. The dentist is available from 3 PM to 9 PM."
* **Workflow:** A step-by-step script for the conversation flow, from greeting to confirmation.

This level of detail ensures the agent stays on track, maintains its persona, and successfully achieves its goal.

#### 2. The Task-Oriented Agent

For transactional tasks, the prompt is highly focused on a specific workflow.

* **Strict Constraints:** It's given rules like, "You will never reply with more than 2 sentences at a time," to keep the interaction moving quickly.
* **Built-in Knowledge:** The prompt contains the full menu with prices and customization options. The agent doesn't have to "think"; it just retrieves information from its core instructions.
* **Upsell Logic:** It's explicitly programmed with business logic, like, "If the customer orders a sandwich, ask: 'Would you like to convert that into a meal for an additional 10 Dirhams?'"

This shows that a prompt isn't just about personality; it's also about embedding business rules directly into the conversation.

<figure><img src="https://i.ibb.co/39WbGq5B/Task-agent-ai-persona.png" alt="KFC Order Taker Agent Workflow"/><figcaption> Task-Oriented agent Persona flow</figcaption></figure>

#### 3. The Empathetic Companion (Hume AI's Approach)

At the frontier of voice AI are agents designed not just to talk, but to sense and respond to human emotion.

* **Emotional Intelligence:** The prompt includes instructions like, "Your communication style is warm, patient, and empathetic. You aim to make the customer feel heard, understood and valued."
* **Responding to Expressions:** Some advanced agents can receive metadata about the user's tone. Their prompt might say, "Analyze the user's emotional expressions... to inform your response," allowing them to react with empathy to frustration or share in a user's excitement.
* **The "No Yapping" Rule:** A brilliant and direct instruction seen in some Hume prompts is `<no_yapping>`. It commands the AI to "be succinct, get straight to the point... NEVER talk too much, users find it painful." This is a perfect example of designing for a better user experience.

<figure><img src="https://i.ibb.co/BpLrw7h/customer-persona-ai.png" alt="AI Customer Service Agent Workflow"/><figcaption> AI customer service agent Persona flow</figcaption></figure>

### The Future is a Conversation

Crafting a great voice AI is a blend of psychology, scriptwriting, and technical design. It's about moving beyond simple command-and-response and building systems that can manage a conversation, maintain a persona, and handle the messy reality of human speech.

As the technology continues to evolve, the quality of our interactions with AI will be determined not just by the power of the models, but by the thoughtful, human-centered design of the prompts that guide them. The future of AI isn't just about what it knows; it's about how it talks.


#### Written by - [Jyotsna Shrivastava](https://www.linkedin.com/in/jyotsna-shrivastava-78b5192b2/)

#### Tags
<a>
<img alt="voice-ai" src="https://img.shields.io/badge/voice-AI-8A2BE2" />
<a>
<img alt="conversational-ai" src="https://img.shields.io/badge/conversational-AI-8A2BE2" />
<a>
<img alt="conversational-ai" src="https://img.shields.io/badge/Prompt-Engineering-8A2BE2" />
<a>
<img alt="conversational-ai" src="https://img.shields.io/badge/Persona-Design-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.
