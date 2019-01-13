from mamba import description, context, it
from expects import expect, equal
from handlers import *

with description('Handlers') as self:
    with it('handles posted_comment'):
        handler = PostedComment({})
        expect(handler.run()).to(equal('OK'))
