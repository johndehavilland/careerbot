# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import ConfirmPrompt, TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from .cancel_and_help_dialog import CancelAndHelpDialog
from .date_resolver_dialog import DateResolverDialog
from datatypes_date_time.timex import Timex

class JobSearchDialog(CancelAndHelpDialog):

    def __init__(self, dialog_id: str = None):
        super(JobSearchDialog, self).__init__(dialog_id or JobSearchDialog.__name__)

        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(DateResolverDialog(DateResolverDialog.__name__))
        self.add_dialog(WaterfallDialog(WaterfallDialog.__name__, [
            self.location_step,
            self.jobtype_step,
            self.final_step
        ]))

        self.initial_dialog_id = WaterfallDialog.__name__
    
    """
    If a location has not been provided, prompt for one.
    """
    async def location_step(self, step_context: WaterfallStepContext) -> DialogTurnResult: 
        job_search = step_context.options

        if (job_search.location is None): 
            return await step_context.prompt(TextPrompt.__name__, PromptOptions(prompt= MessageFactory.text('What city are you interested in?')))
        else: 
            return await step_context.next(job_search.location)

    """
    If a job type has not been provided, prompt for one.
    """
    async def jobtype_step(self, step_context: WaterfallStepContext) -> DialogTurnResult: 
        job_search = step_context.options

        # Capture the response to the previous step's prompt
        job_search.location = step_context.result
        if (job_search.jobtype is None): 
            return await step_context.prompt(TextPrompt.__name__, PromptOptions(prompt= MessageFactory.text('What types of jobs are you interested in?')))
        else: 
            return await step_context.next(job_search.jobtype)

    """
    Complete the interaction and end the dialog.
    """
    async def final_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:

        if step_context.result: 
            job_search = step_context.options
            job_search.jobtype = step_context.result
            return await step_context.end_dialog(job_search)
        else: 
            return await step_context.end_dialog()

    def is_ambiguous(self, timex: str) -> bool: 
        timex_property = Timex(timex)
        return 'definite' not in timex_property.types


    
    