
# This module defines the global constants.


import os
import getpass
import tempfile


HTTP_FORBIDDEN = 403

COURSERA_URL = 'https://api.coursera.org'
AUTH_URL = 'https://accounts.coursera.org/api/v1/login'
AUTH_URL_V3 = 'https://api.coursera.org/api/login/v3'
CLASS_URL = 'https://class.coursera.org/{class_name}'

OPENCOURSE_LIST_COURSES = 'https://api.coursera.org/api/courses.v1?q=watchlist&start={start}'


OPENCOURSE_MEMBERSHIPS = 'https://api.coursera.org/api/memberships.v1?includes=courseId,courses.v1&q=me&showHidden=true&filter=current,preEnrolled'
OPENCOURSE_ONDEMAND_LECTURE_VIDEOS_URL = \
    'https://api.coursera.org/api/onDemandLectureVideos.v1/'\
    '{course_id}~{video_id}?includes=video&'\
    'fields=onDemandVideos.v1(sources%2Csubtitles%2CsubtitlesVtt%2CsubtitlesTxt)'
OPENCOURSE_SUPPLEMENT_URL = 'https://api.coursera.org/api/onDemandSupplements.v1/'\
    '{course_id}~{element_id}?includes=asset&fields=openCourseAssets.v1%28typeName%29,openCourseAssets.v1%28definition%29'
OPENCOURSE_PROGRAMMING_ASSIGNMENTS_URL = \
    'https://api.coursera.org/api/onDemandProgrammingLearnerAssignments.v1/{course_id}~{element_id}?fields=submissionLearnerSchema'
OPENCOURSE_PROGRAMMING_IMMEDIATE_INSTRUCTIOINS_URL = \
    'https://api.coursera.org/api/onDemandProgrammingImmediateInstructions.v1/{course_id}~{element_id}'
OPENCOURSE_REFERENCES_POLL_URL = \
    "https://api.coursera.org/api/onDemandReferences.v1/?courseId={course_id}&q=courseListed&fields=name%2CshortId%2Cslug%2Ccontent&includes=assets"
OPENCOURSE_REFERENCE_ITEM_URL = \
    "https://api.coursera.org/api/onDemandReferences.v1/?courseId={course_id}&q=shortId&shortId={short_id}&fields=name%2CshortId%2Cslug%2Ccontent&includes=assets"


OPENCOURSE_ASSET_URL = \
    'https://api.coursera.org/api/assetUrls.v1?ids={ids}'


OPENCOURSE_ONDEMAND_LECTURE_ASSETS_URL = \
    'https://api.coursera.org/api/onDemandLectureAssets.v1/'\
    '{course_id}~{video_id}/?includes=openCourseAssets'

OPENCOURSE_ASSETS_URL = \
    'https://api.coursera.org/api/openCourseAssets.v1/{id}'

OPENCOURSE_API_ASSETS_V1_URL = \
    'https://api.coursera.org/api/assets.v1?ids={id}'

OPENCOURSE_ONDEMAND_COURSE_MATERIALS = \
    'https://api.coursera.org/api/onDemandCourseMaterials.v1/?'\
    'q=slug&slug={class_name}&includes=moduleIds%2ClessonIds%2CpassableItemGroups%2CpassableItemGroupChoices%2CpassableLessonElements%2CitemIds%2Ctracks'\
    '&fields=moduleIds%2ConDemandCourseMaterialModules.v1(name%2Cslug%2Cdescription%2CtimeCommitment%2ClessonIds%2Coptional)%2ConDemandCourseMaterialLessons.v1(name%2Cslug%2CtimeCommitment%2CelementIds%2Coptional%2CtrackId)%2ConDemandCourseMaterialPassableItemGroups.v1(requiredPassedCount%2CpassableItemGroupChoiceIds%2CtrackId)%2ConDemandCourseMaterialPassableItemGroupChoices.v1(name%2Cdescription%2CitemIds)%2ConDemandCourseMaterialPassableLessonElements.v1(gradingWeight)%2ConDemandCourseMaterialItems.v1(name%2Cslug%2CtimeCommitment%2Ccontent%2CisLocked%2ClockableByItem%2CitemLockedReasonCode%2CtrackId)%2ConDemandCourseMaterialTracks.v1(passablesCount)'\
    '&showLockedItems=true'

OPENCOURSE_ONDEMAND_COURSE_MATERIALS_V2 = \
    'https://api.coursera.org/api/onDemandCourseMaterials.v2/?q=slug&slug={class_name}'\
    '&includes=modules%2Clessons%2CpassableItemGroups%2CpassableItemGroupChoices%2CpassableLessonElements%2Citems%2Ctracks%2CgradePolicy&'\
    '&fields=moduleIds%2ConDemandCourseMaterialModules.v1(name%2Cslug%2Cdescription%2CtimeCommitment%2ClessonIds%2Coptional%2ClearningObjectives)%2ConDemandCourseMaterialLessons.v1(name%2Cslug%2CtimeCommitment%2CelementIds%2Coptional%2CtrackId)%2ConDemandCourseMaterialPassableItemGroups.v1(requiredPassedCount%2CpassableItemGroupChoiceIds%2CtrackId)%2ConDemandCourseMaterialPassableItemGroupChoices.v1(name%2Cdescription%2CitemIds)%2ConDemandCourseMaterialPassableLessonElements.v1(gradingWeight%2CisRequiredForPassing)%2ConDemandCourseMaterialItems.v2(name%2Cslug%2CtimeCommitment%2CcontentSummary%2CisLocked%2ClockableByItem%2CitemLockedReasonCode%2CtrackId%2ClockedStatus%2CitemLockSummary)%2ConDemandCourseMaterialTracks.v1(passablesCount)'\
    '&showLockedItems=true'

OPENCOURSE_ONDEMAND_SPECIALIZATIONS_V1 = \
    'https://api.coursera.org/api/onDemandSpecializations.v1?q=slug'\
    '&slug={class_name}&fields=courseIds,interchangeableCourseIds,launchedAt,'\
    'logo,memberships,metadata,partnerIds,premiumExperienceVariant,'\
    'onDemandSpecializationMemberships.v1(suggestedSessionSchedule),'\
    'onDemandSpecializationSuggestedSchedule.v1(suggestedSessions),'\
    'partners.v1(homeLink,name),courses.v1(courseProgress,description,'\
    'membershipIds,startDate,v2Details,vcMembershipIds),v2Details.v1('\
    'onDemandSessions,plannedLaunchDate),memberships.v1(grade,'\
    'vcMembershipId),vcMemberships.v1(certificateCodeWithGrade)'\
    '&includes=courseIds,memberships,partnerIds,'\
    'onDemandSpecializationMemberships.v1(suggestedSessionSchedule),'\
    'courses.v1(courseProgress,membershipIds,v2Details,vcMembershipIds),'\
    'v2Details.v1(onDemandSessions)'

OPENCOURSE_ONDEMAND_COURSES_V1 = \
    'https://api.coursera.org/api/onDemandCourses.v1?q=slug&slug={class_name}&'\
    'includes=instructorIds%2CpartnerIds%2C_links&'\
    'fields=brandingImage%2CcertificatePurchaseEnabledAt%2Cpartners.v1(squareLogo%2CrectangularLogo)%2Cinstructors.v1(fullName)%2CoverridePartnerLogos%2CsessionsEnabledAt%2CdomainTypes%2CpremiumExperienceVariant%2CisRestrictedMembership'

ABOUT_URL = ('https://api.coursera.org/api/catalog.v1/courses?'
             'fields=largeIcon,photo,previewLink,shortDescription,smallIcon,'
             'smallIconHover,universityLogo,universityLogoSt,video,videoId,'
             'aboutTheCourse,targetAudience,faq,courseSyllabus,courseFormat,'
             'suggestedReadings,instructor,estimatedClassWorkload,'
             'aboutTheInstructor,recommendedBackground,subtitleLanguagesCsv&'
             'q=search&query={class_name}')

AUTH_REDIRECT_URL = ('https://class.coursera.org/{class_name}'
                     '/auth/auth_redirector?type=login&subtype=normal')


OPENCOURSE_PEER_ASSIGNMENT_INSTRUCTIONS = (
    'https://api.coursera.org/api/onDemandPeerAssignmentInstructions.v1/?'
    'q=latest&userId={user_id}&courseId={course_id}&itemId={element_id}&'
    'includes=gradingMetadata%2CreviewSchemas%2CsubmissionSchemas&'
    'fields=instructions%2ConDemandPeerAssignmentGradingMetadata.v1(requiredAuthoredReviewCount%2CisMentorGraded%2CassignmentDetails)%2ConDemandPeerReviewSchemas.v1(reviewSchema)%2ConDemandPeerSubmissionSchemas.v1(submissionSchema)')

POST_OPENCOURSE_API_QUIZ_SESSION = 'https://api.coursera.org/api/opencourse.v1/user/{user_id}/course/{class_name}/item/{quiz_id}/quiz/session'

POST_OPENCOURSE_API_QUIZ_SESSION_GET_STATE = 'https://api.coursera.org/api/opencourse.v1/user/{user_id}/course/{class_name}/item/{quiz_id}/quiz/session/{session_id}/action/getState?autoEnroll=false'

POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS = 'https://api.coursera.org/api/onDemandExamSessions.v1'

POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS_GET_STATE = 'https://api.coursera.org/api/onDemandExamSessions.v1/{session_id}/actions?includes=gradingAttempts'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# define a per-user cache folder
if os.name == "posix":  # pragma: no cover
    import pwd
    _USER = pwd.getpwuid(os.getuid())[0]
else:
    _USER = getpass.getuser()

PATH_CACHE = os.path.join(tempfile.gettempdir(), _USER + "_coursera_dl_cache")
PATH_COOKIES = os.path.join(PATH_CACHE, 'cookies')

WINDOWS_UNC_PREFIX = u'\\\\?\\'

IN_MEMORY_EXTENSION = 'html'

IN_MEMORY_MARKER = '#inmemory#'

FORMAT_MAX_LENGTH = 20
TITLE_MAX_LENGTH = 200

INSTRUCTIONS_HTML_INJECTION_PRE = '''
<style>
body {
    padding: 50px 85px 50px 85px;
}

table th, table td {
    border: 1px solid #e0e0e0;
    padding: 5px 20px;
    text-align: left;
}
input {
    margin: 10px;
}
}
th {
    font-weight: bold;
}
td, th {
    display: table-cell;
    vertical-align: inherit;
}
img {
    height: auto;
    max-width: 100%;
}
pre {
    display: block;
    margin: 20px;
    background: #424242;
    color: #fff;
    font-size: 13px;
    white-space: pre-wrap;
    padding: 9.5px;
    margin: 0 0 10px;
    border: 1px solid #ccc;
}
</style>

<script type="text/javascript" async
  src="'''
INSTRUCTIONS_HTML_MATHJAX_URL = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js'
INSTRUCTIONS_HTML_INJECTION_AFTER = '''?config=TeX-AMS-MML_HTMLorMML">
</script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$$','$$'], ['$','$'] ],
      displayMath: [ ["\\\\[","\\\\]"] ],
      processEscapes: true
    }
  });
</script>
'''

# The following url is the root url (tree) for a Coursera Course
OPENCOURSE_NOTEBOOK_DESCRIPTIONS = "https://hub.coursera-notebooks.org/hub/coursera_login?token={authId}&next=/"
OPENCOURSE_NOTEBOOK_LAUNCHES = "https://api.coursera.org/api/onDemandNotebookWorkspaceLaunches.v1/?fields=authorizationId%2CcontentPath%2CuseLegacySystem"
OPENCOURSE_NOTEBOOK_TREE = "https://hub.coursera-notebooks.org/user/{jupId}/api/contents/{path}?type=directory&_={timestamp}"
OPENCOURSE_NOTEBOOK_DOWNLOAD = "https://hub.coursera-notebooks.org/user/{jupId}/files/{path}?download=1"
