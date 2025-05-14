SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;
ALTER SCHEMA public OWNER TO pg_database_owner;

CREATE TYPE public.user_profile_enum AS ENUM (
    'UserAdmin',
    'Cleaner',
    'HomeOwner',
    'PlatformManagement'
);

ALTER TYPE public.user_profile_enum OWNER TO postgres;

SET default_tablespace = '';
SET default_table_access_method = heap;

CREATE TABLE public."Category" (
    "CategoryID" integer NOT NULL,
    "Title" text,
    "Description" text,
    "Is_Active" boolean DEFAULT true NOT NULL
);

ALTER TABLE public."Category" OWNER TO postgres;

CREATE SEQUENCE public."CategoryID"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public."CategoryID" OWNER TO postgres;

CREATE TABLE public."Matches" (
    "ServiceID" integer NOT NULL,
    "HomeOwnerID" integer NOT NULL,
    "Price" double precision,
    "Date" timestamp with time zone DEFAULT now() NOT NULL,
    "Rating" integer
);

ALTER TABLE public."Matches" OWNER TO postgres;

CREATE TABLE public."Service" (
    "ServiceID" integer NOT NULL,
    "CategoryID" integer NOT NULL,
    "Title" character varying NOT NULL,
    "Description" text NOT NULL,
    "DatePosted" timestamp with time zone DEFAULT now() NOT NULL,
    "CleanerID" integer NOT NULL,
    "LikeCount" integer DEFAULT 0 NOT NULL,
    "ViewCount" integer DEFAULT 0 NOT NULL,
    "MatchCount" integer DEFAULT 0 NOT NULL,
    price double precision NOT NULL,
    "ImageLink" text
);

ALTER TABLE public."Service" OWNER TO postgres;

CREATE SEQUENCE public."ServiceID_Seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public."ServiceID_Seq" OWNER TO postgres;

CREATE TABLE public."Shortlist_Record" (
    "ServiceID" integer NOT NULL,
    "HomeOwnerID" integer NOT NULL
);

ALTER TABLE public."Shortlist_Record" OWNER TO postgres;

CREATE TABLE public."UserProfile" (
    "UserProfileID" integer NOT NULL,
    "Name" text NOT NULL,
    "Privilege" text NOT NULL,
    "Is_Active" boolean DEFAULT true NOT NULL
);

ALTER TABLE public."UserProfile" OWNER TO postgres;

CREATE SEQUENCE public."UserProfile_UserProfileID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public."UserProfile_UserProfileID_seq" OWNER TO postgres;

CREATE TABLE public."Views" (
    "HomeOwnerID" integer NOT NULL,
    "ServiceID" integer NOT NULL
);

ALTER TABLE public."Views" OWNER TO postgres;

CREATE TABLE public."user" (
    "UserID" integer NOT NULL,
    "Username" character varying,
    "Email" character varying,
    "Phone" character varying,
    "Password" character varying,
    "IsActive" boolean,
    "UserProfileID" integer NOT NULL,
    "Address" text,
    "Experience" numeric
);

ALTER TABLE public."user" OWNER TO postgres;

CREATE SEQUENCE public."user_UserID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public."user_UserID_seq" OWNER TO postgres;

ALTER TABLE ONLY public."Category"
    ADD CONSTRAINT "Category_pkey" PRIMARY KEY ("CategoryID");

ALTER TABLE ONLY public."Service"
    ADD CONSTRAINT "Service_pkey" PRIMARY KEY ("ServiceID");

ALTER TABLE ONLY public."Category"
    ADD CONSTRAINT "Unique Title" UNIQUE ("Title");

ALTER TABLE ONLY public."UserProfile"
    ADD CONSTRAINT "Unique UserProfileName" UNIQUE ("Name");

ALTER TABLE ONLY public."Service"
    ADD CONSTRAINT "Unique_Title_service" UNIQUE ("Title");

ALTER TABLE ONLY public."UserProfile"
    ADD CONSTRAINT "UserProfile_pkey" PRIMARY KEY ("UserProfileID");

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT "user_Username_key" UNIQUE ("Username");

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY ("UserID");

CREATE UNIQUE INDEX "Shortlist_Record_ServiceID_HomeOwnerID_idx" ON public."Shortlist_Record" USING btree ("ServiceID", "HomeOwnerID");

GRANT USAGE ON SCHEMA public TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Category" TO root;

GRANT ALL ON SEQUENCE public."CategoryID" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Matches" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Service" TO root;

GRANT ALL ON SEQUENCE public."ServiceID_Seq" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Shortlist_Record" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."UserProfile" TO root;

GRANT SELECT,USAGE ON SEQUENCE public."UserProfile_UserProfileID_seq" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Views" TO root;

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."user" TO root;

GRANT ALL ON SEQUENCE public."user_UserID_seq" TO root;

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES TO root;