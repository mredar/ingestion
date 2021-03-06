from akara import logger
from dplaingestion.utilities import iterify
from dplaingestion.selector import exists, getprop
from dplaingestion.mappers.mapper import Mapper

class UNTLMapper(Mapper):
    def __init__(self, provider_data, key_prefix="untl:"):
        super(UNTLMapper, self).__init__(provider_data, key_prefix)
        self.root_key = "metadata/metadata/"
        self.rights_term_label = {
            "by": "Attribution.",
            "by-nc": "Attribution Noncommercial.",
            "by-nc-nd": "Attribution Non-commercial No Derivatives.",
            "by-nc-sa": "Attribution Noncommercial Share Alike.",
            "by-nd": "Attribution No Derivatives.",
            "by-sa": "Attribution Share Alike.",
            "copyright": "Copyright.",
            "pd": "Public Domain."
        }
        self.dataprovider_term_label = {
            "ABB": "Bryan Wildenthal Memorial Library (Archives of the " + \
                   "Big Bend)",
            "ABPL": "Abilene Public Library",
            "ACGS": "Anderson County Genealogical Society",
            "ACHC": "Anderson County Historical Commission",
            "ACRM": "Amon Carter Museum",
            "ACTUMT": "Archives of the Central Texas Conference United " + \
                      "Methodist Church",
            "ACUL": "Abilene Christian University Library",
            "APL": "Alvord Public Library",
            "ASPL": "Austin History Center, Austin Public Library",
            "ASTC": "Austin College",
            "BCHC": "Bosque County Historical Commission",
            "BDPL": "Boyce Ditto Public Library",
            "BPL": "Lena Armstrong Public Library",
            "CCGS": "Collin County Genealogical Society",
            "CCHM": "North Texas History Center",
            "CCHS": "Clay County Historical Society",
            "CCMH": "Childress County Heritage Museum",
            "CCMS": "Corpus Christi Museum of Science and History",
            "CHM": "Clark Hotel Museum",
            "CHOS": "Courthouse-on-the-Square Museum",
            "CTRM": "Cattle Raisers Museum",
            "CUA": "Concordia University at Austin",
            "CWTC": "Cowtown Coliseum",
            "DAPL": "Dallas Public Library",
            "DHS": "Dallas Historical Society",
            "DHVG": "Dallas Heritage Village",
            "DPL": "Denton Public Library",
            "DSCL": "Deaf Smith County Library",
            "EPL": "Euless Public Library",
            "ETGS": "East Texas Genealogical Society",
            "FBCM": "FBC Heritage Museum",
            "FBM": "Fort Bend Museum",
            "FCPA": "First Christian Church of Port Arthur",
            "FPL": "Ferris Public Library",
            "FWJA": "Fort Worth Jewish Archives",
            "FWPL": "Fort Worth Public Library",
            "GLO": "Texas General Land Office",
            "GMHP": "Genevieve Miller Hitchcock Public Library",
            "GR": "George Ranch Historical Park",
            "HCGS": "Hutchinson County Genealogical Society",
            "HHSM": "Heritage House Museum",
            "HPUL": "Howard Payne University Library",
            "HSUL": "Hardin-Simmons University Library",
            "IPL": "Irving Archives",
            "JFRM": "Jacob Fontaine Religious Museum",
            "KCT": "Killeen City Library System",
            "KHSY": "Kemah Historical Society",
            "KUMC": "Krum United Methodist Church",
            "LCVG": "Log Cabin Village",
            "LDMA": "Lockheed Martin Aeronautics Company, Fort Worth",
            "LPL": "Laredo Public Library",
            "MARD": "Museum of the American Railroad",
            "MFAH": "The Museum of Fine Arts, Houston",
            "MMMM": "Medicine Mound Museum",
            "MMPL": "Moore Memorial Public Library",
            "MMUL": "McMurry University Library",
            "MPLI": "Marshall Public Library",
            "MRPL": "Marfa Public Library",
            "OKHS": "Oklahoma Historical Society",
            "OSAGC": "Old Settler's Association of Grayson County",
            "PANAM": "The University of Texas-Pan American",
            "PCBG": "Private Collection of Bouncer Goin",
            "PCCRD": "Private Collection of Charles R. Delphenis",
            "PCCRS": "Private Collection of Caroline R. Scrivner Richards",
            "PCHBM": "Private Collection of Howard and Brenda McClurkin",
            "PCJEH": "Private Collection of Joe E. Haynes",
            "PPL": "Palestine Public Library",
            "RPL": "Richardson Public Library",
            "RSMT": "Rose Marine Theatre",
            "SJMH": "San Jacinto Museum of History",
            "SMU": "Southern Methodist University Libraries",
            "SRPL": "Sanger Public Library",
            "STAR": "Star of the Republic Museum",
            "SSPL": "Sulphur Springs Public Library",
            "TCC": "Tarrant County College NE, Heritage Room",
            "TCU": "Texas Christian University",
            "TSGS": "Texas State Genealogical Society",
            "TSLAC": "Texas State Library and Archives Commission",
            "TWU": "Texas Woman's University",
            "TXLU": "Texas Lutheran University",
            "UH": "University of Houston Libraries' Special Collections",
            "UNT": "UNT Libraries",
            "UT": "University of Texas",
            "UTA": "University of Texas at Arlington Library",
            "UTSW": "UT Southwestern Medical Center Library",
            "VCHC": "Val Verde County Historical Commission",
            "WCHM": "Wolf Creek Heritage Museum",
            "WEAC": "Weatherford College",
            "WEBM": "Weslaco Museum",
            "OTHER": "Other",
            "RICE": "Rice University Woodson Research Center",
            "HCDC": "Henderson County District Clerk's Office",
            "ORMM": "The Old Red Museum",
            "SFMDP": "The Sixth Floor Museum at Dealey Plaza",
            "CCTX": "City of Clarendon",
            "PCEBF": "The Private Collection of the Ellis and Blanton " + \
                     "Families",
            "DCCCD": "Dallas County Community College District",
            "THF": "Texas Historical Foundation",
            "SWCL": "Swisher County Library",
            "WYU": "Wiley College",
            "LBJSM": "LBJ Museum of San Marcos",
            "DSMA": "Dallas Municipal Archives",
            "FRLM": "French Legation Museum ",
            "PCSF": "The Private Collection of the Sutherlin Family",
            "ARPL": "Arlington Public Library and Fielder House",
            "BEHC": "Bee County Historical Commission",
            "CGHPC": "City of Granbury Historic Preservation Commission",
            "ELPL": "El Paso Public Library ",
            "GPHO": "Grand Prairie Historical Organization",
            "MLCC": "Matthews Family and Lambshead Ranch",
            "NELC": "Northeast Lakeview College",
            "PAPL": "Port Arthur Public Library",
            "PBPM": "Permian Basin Petroleum Museum, Library and Hall of Fame",
            "RVPM": "River Valley Pioneer Museum",
            "SFASF": "Stephen F. Austin Assn. dba Friends of the San " + \
                     "Felipe State Historic Site",
            "UTSA": "University of Texas at San Antonio",
            "VCUH": "Victoria College/University of Houston-Victoria Library",
            "HCLY": "Hemphill County Library",
            "BACHS": "Bartlett Activities Center and the Historical " + \
                     "Society of Bartlett",
            "CAH": "The Dolph Briscoe Center for American History ",
            "UNTA": "UNT Archives",
            "UNTRB": "UNT Libraries Rare Book and Texana Collections",
            "UNTCVA": "UNT College of Visual Arts + Design",
            "UNTDP": "UNT Libraries Digital Projects Unit",
            "UNTGD": "UNT Libraries Government Documents Department",
            "UNTML": "UNT Music Library",
            "UNTP": "UNT Press",
            "UNTLML": "UNT Media Library",
            "UNTCOI": "UNT College of Information",
            "BRPL": "Breckenridge Public Library",
            "STWCL": "Stonewall County Library",
            "NPSL": "Nicholas P. Sims Library",
            "PCJB": "Private Collection of Jim Bell",
            "MQPL": "Mesquite Public Library",
            "BWPL": "Bell/Whittington Public Library",
            "CHMH": "Cedar Hill Museum of History",
            "CLHS": "Cleveland Historic Society",
            "CKCL": "Cooke County Library",
            "DFFM": "Dallas Firefighters Museum",
            "FSML": "Friench Simpson Memorial Library",
            "HSCA": "Harris County Archives",
            "HTPL": "Haslet Public Library",
            "LVPL": "Longview Public Library",
            "MWSU": "Midwestern State University",
            "STPC": "St. Philips College",
            "UTHSC": "University of Texas Health Science Center Libraries",
            "WCHS": "Wilson County Historical Society",
            "TSHA": "Texas State Historical Association",
            "MCMPL": "McAllen Public Library",
            "UNTLTC": "UNT Linguistics and Technical Communication Department",
            "PCMB": "Private Collection of Melvin E. Brewer",
            "SGML": "Singletary Memorial Library",
            "URCM": "University Relations, Communications & Marketing " + \
                    "department for UNT",
            "TXDTR": "Texas Department of Transportation",
            "TYPL": "Taylor Public Library",
            "WILLM": "The Williamson Museum",
            "ATPS": "Austin Presbyterian Theological Seminary",
            "BUCHC": "Burnet County Historical Commission",
            "DHPS": "Danish Heritage Preservation Society",
            "GCHS": "Gillespie County Historical Society",
            "HMRC": "Houston Metropolitan Research Center at Houston " + \
                    "Public Library",
            "ITC": "University of Texas at San Antonio Libraries Special " + \
                   "Collections",
            "DISCO": "Digital Scholarship Cooperative (DiSCo)",
            "MAMU": "Mexic-Arte Museum",
            "MMLUT": "Moody Medical Library, UT",
            "MGC": "Museum of the Gulf Coast",
            "NML": "Nesbitt Memorial Library",
            "PAC": "Panola College ",
            "PJFC": "Price Johnson Family Collection",
            "SAPL": "San Antonio Public Library",
            "AMSC": "Anne and Mike Stewart Collection",
            "TSU": "Tarleton State University",
            "STPRB": "Texas State Preservation Board",
            "UNTCAS": "UNT College of Arts and Sciences",
            "UNTCOE": "UNT College of Engineering",
            "UNTCPA": "UNT College of Public Affairs and Community Service",
            "STXCL": "South Texas College of Law",
            "CPL": "Carrollton Public Library",
            "CWCM": "Collingsworth County Museum",
            "PCMC": "Private Collection of Mike Cochran",
            "NMPW": "National Museum of the Pacific War/Admiral Nimitz " + \
                    "Foundation",
            "SRH": "Sam Rayburn House Museum",
            "TCFA": "Talkington Clement Family Archives",
            "WTM": "Witte Museum",
            "UNTCED": "UNT College of Education",
            "BECA": "Beth-El Congregation Archives",
            "UNTCEDR": "UNT Center for Economic Development and Research",
            "DMA": "Dallas Museum of Art",
            "UTMDAC": "University of Texas MD Anderson Center",
            "UNTSMHM": "UNT College of Merchandising, Hospitality and Tourism",
            "UTEP": "University of Texas at El Paso",
            "UNTHSC": "UNT Health Science Center",
            "PPHM": "Panhandle-Plains Historical Museum",
            "AMPL": "Amarillo Public Library",
            "FWHC": "The History Center",
            "EFNHM": "Elm Fork Natural Heritage Museum",
            "UNTOHP": "UNT Oral History Program",
            "UNTCOB": "UNT College of Business ",
            "HCLB": "Hutchinson County Library, Borger Branch",
            "HPWML": "Harrie P. Woodson Memorial Library",
            "CTLS": "Central Texas Library System",
            "ARMCM": "Armstrong County Museum",
            "CHRK": "Cherokeean Herald",
            "DGS": "Dallas Genealogical Society",
            "UNTCOM": "UNT College of Music ",
            "MBIGB": "Museum of the Big Bend",
            "SCPL": "Schulenburg Public Library",
            "UNTCEP": "UNT Center For Environmental Philosophy",
            "UDAL": "University of Dallas",
            "PVAMU": "Prairie View A&M University ",
            "TWSU": "Texas Wesleyan University",
            "RGPL": "Rio Grande City Public Library",
            "UNTIAS": "UNT Institute of Applied Sciences",
            "UNTGSJ": "UNT Frank W. and Sue Mayborn School of Journalism",
            "BSTPL": "Bastrop Public Library",
            "SHML": "Stella Hill Memorial Library",
            "CAL": "Canyon Area Library",
            "MWHA": "Mineral Wells Heritage Association",
            "TAEA": "Texas Art Education Association",
            "EPCHS": "El Paso County Historical Society ",
            "CPPL": "Cross Plains Public Library",
            "LCHHL": "League City Helen Hall Library",
            "NCWM": "National Cowboy and Western Heritage Museum",
            "SWATER": "Sweetwater/Nolan County City-County Library",
            "UNTHON": "UNT Honors College",
            "PCJW": "Private Collection of Judy Wood and Jim Atkinson",
            "CRPL": "Crosby County Public Library",
            "DPKR": "City of Denton Parks and Recreation",
            "THC": "Texas Historical Commission",
            "BSAM": "Boy Scouts of America National Scouting Museum",
            "PCCW": "Private Collection of Carolyn West",
            "OCHS": "Orange County Historical Society",
            "DISD": "Denton Independent School District",
            "MINML": "Mineola Memorial Library",
            "CASML": "Casey Memorial Library",
            "UNTD": "UNT Dallas",
            "PTBW": "Private Collection of T. Bradford Willis",
            "UNTG": "University of North Texas Galleries",
            "SCHU": "Schreiner University",
            "TYHL": "Tyrrell Historical Library ",
            "TCAF": "Texas Chapter of the American Fisheries Society",
            "GIBBS": "Gibbs Memorial Library",
            "ATLANT": "Atlanta Public Library",
            "CCS": "City of College Station",
            "GCFV": "Grayson County Frontier Village",
            "PCTF": "Private Collection of the Tarver Family",
            "TAMS": "Texas Academy of Mathematics and Science",
            "CCHC": "Cherokee County Historical Commission",
            "PCBARTH": "Private Collection of Marie Bartholomew",
            "CCPL": "Corpus Christi Public Library",
            "UNTDCL": "UNT Dallas College of Law",
            "LAMAR": "Lamar State College - Orange",
            "SDEC": "St. David's Episcopal Church",
            "TDCD": "Travis County District Clerk's Office"
        }

    def map_date(self):
        """
        Use the first instance of untl:date where the qualifier == "creation"
        otherwhise use the first instance of untl:date where
        qualifier != "digitized" or qualifier != "embargoUntil"
        """

        prop = self.root_key + "date"

        if exists(self.provider_data, prop):
            date = None

            creation_date = None
            non_digitized_embargo_until_date = None
            for s in iterify(getprop(self.provider_data, prop)):
                if "qualifier" in s:
                    if s["qualifier"] == "creation":
                        creation_date = s.get("#text")
                        break
                    elif (s["qualifier"] not in
                          ["digitized", "embargoUntil"] and \
                          non_digitized_embargo_until_date is None):
                        non_digitized_embargo_until_date = s.get("#text")

            if creation_date is not None:
                date = creation_date
            else:
                date = non_digitized_embargo_until_date

            if date:
                self.update_source_resource({"date": date})

    def map_title(self):
        prop = self.root_key + "title"

        if exists(self.provider_data, prop):
            title = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    title.append(s)
                elif "#text" in s:
                    title.append(s["#text"])

            if title:
                self.update_source_resource({"title": title})

    def map_rights(self):
        prop = self.root_key + "rights"

        if exists(self.provider_data, prop):
            rights = None
            license = None
            statement = None
            for s in iterify(getprop(self.provider_data, prop)):
                try:
                    qualifier = s.get("qualifier")
                    text = s.get("#text")
                except:
                    continue

                if qualifier == "license":
                    try:
                        license = "License: " + self.rights_term_label[text]
                    except:
                        msg = ("Term %s not in self.rights_term_label for %s" %
                               (text, self.provider_data["_id"]))
                        logger.error(msg)
                elif qualifier == "statement":
                    statement = text

            rights = "; ".join(filter(None, [rights, statement]))

            if rights:
                self.update_source_resource({"rights": rights})

    def map_type(self):
        prop = self.root_key + "format"

        if exists(self.provider_data, prop):
            format_to_type = {
                "audio": "sound",
                "video": "moving image",
                "website": "interactive resource"
            }

            _type = []
            for s in iterify(getprop(self.provider_data, prop)):
                if s == "other":
                    pass
                elif s in format_to_type.keys():
                    _type.append(format_to_type[s])
                else:
                    _type.append(s)

            if _type:
                self.update_source_resource({"type": _type})

    def map_creator(self):
        prop = self.root_key + "creator"

        if exists(self.provider_data, prop):
            creator = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    creator.append(s)
                elif "name" in s:
                    creator.append(s["name"])

            if creator:
                self.update_source_resource({"creator": creator})

    def map_subject(self):
        prop = self.root_key + "subject"

        if exists(self.provider_data, prop):
            subject = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    subject.append(s)
                elif "#text" in s:
                    subject.append(s["#text"])

            if subject:
                self.update_source_resource({"subject": " - ".join(subject)})

    def map_relation(self):
        prop = self.root_key + "relation"

        if exists(self.provider_data, prop):
            relation = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    relation.append(s)
                elif "#text" in s:
                    relation.append(s["#text"])

            if relation:
                self.update_source_resource({"relation": relation})

    def map_spatial(self):
        prop = self.root_key + "coverage"

        if exists(self.provider_data, prop):
            spatial = []
            qualifiers = ["placeName", "placePoint", "placeBox"]
            for s in iterify(getprop(self.provider_data, prop)):
                if "qualifier" in s and s["qualifier"] in qualifiers:
                    spatial.append(s.get("#text"))
            spatial = filter(None, spatial)

            if spatial:
                self.update_source_resource({"spatial": spatial})

    def map_publisher(self):
        prop = self.root_key + "publisher"

        if exists(self.provider_data, prop):
            publisher = []
            for s in iterify(getprop(self.provider_data, prop)):
                if "location" in s and "name" in s:
                    publisher.append("%s: %s" % (s["location"].strip(),
                                                 s["name"].strip()))

            if publisher:
                self.update_source_resource({"publisher": publisher})

    def map_contributor(self):
        prop = self.root_key + "contributor"

        if exists(self.provider_data, prop):
            contributor = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    contributor.append(s)
                elif "name" in s:
                    contributor.append(s["name"])

            if contributor:
                self.update_source_resource({"contributor": contributor})
            else:
                logger.error("No contributor for record %s" %
                             self.provider_data["_id"])

    def map_description(self):
        prop = self.root_key + "description"

        if exists(self.provider_data, prop):
            description = []
            for s in iterify(getprop(self.provider_data, prop)):
                if isinstance(s, basestring):
                    description.append(s)
                elif "#text" in s:
                    description.append(s["#text"])

            if description:
                self.update_source_resource({"description": description})

    def map_language(self):
        prop = self.root_key + "language"

        if exists(self.provider_data, prop):
            self.update_source_resource({"language":
                                         getprop(self.provider_data, prop)})

    def map_data_provider(self):
        prop = "originalRecord/header/setSpec"

        if exists(self.provider_data, prop):
            dataprovider = []
            for s in iterify(getprop(self.provider_data, prop)):
                if "partner" in s:
                    term = s.split(":")[-1]
                    try:
                        dataprovider.append(self.dataprovider_term_label[term])
                    except:
                        logger.debug("Term %s does not exist in " % term +
                                     "self.dataprovider_term_label for %s" %
                                     self.provider_data["_id"])

            if dataprovider:
                self.mapped_data.update({"dataProvider": dataprovider})

    def map_spec_type_and_format(self):
        prop = self.root_key + "resourceType"

        if exists(self.provider_data, prop):
            _dict = {}
            spec_type = None
            for s in iterify(getprop(self.provider_data, prop)):
                values = s.split("_")
                _dict["format"] = values[0]
                try:
                    if values[1] in ["book", "newspaper", "journal"]:
                        spec_type = values[1]
                    elif values[1] == "leg":
                        spec_type = "government document"
                    elif values[1] == "serial":
                        spec_type = "journal"
                except:
                    pass
            if spec_type is not None:
                _dict["specType"] = spec_type.title()

            self.update_source_resource(_dict)

    def map_identifier_object_and_is_shown_at(self):
        prop = self.root_key + "identifier"

        if exists(self.provider_data, prop):
            _dict = {}
            identifier = []
            for s in iterify(getprop(self.provider_data, prop)):
                try:
                    qualifier = s.get("qualifier")
                    text = s.get("#text")
                    if qualifier and text:
                        identifier.append("%s: %s" % (qualifier, text))

                    if qualifier == "itemURL":
                        _dict["isShownAt"] = text
                    elif qualifier == "thumbnailURL":
                        _dict["object"] = text
                except:
                    pass

            if identifier:
                self.update_source_resource({"identifier": identifier})

            self.mapped_data.update(_dict)

    def map_multiple_fields(self):
        self.map_spec_type_and_format()
        self.map_identifier_object_and_is_shown_at()
